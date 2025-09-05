# User Viewing History (partial watch, multiple devices, resume)

**Concepts**:

* A *playback session* per device/profile; fine-grained *events*; a compact *resume state*.

**DDL**:

```sql
CREATE TABLE account (
  account_id BIGINT PRIMARY KEY
);
CREATE TABLE profile (
  profile_id BIGINT PRIMARY KEY,
  account_id BIGINT REFERENCES account(account_id),
  maturity_setting STRING,
  country_code STRING
);
CREATE TABLE device (
  device_id STRING PRIMARY KEY,       -- GUID or device fingerprint
  device_type STRING,                 -- TV, mobile, web
  os_version STRING
);

CREATE TABLE playback_session (
  session_id STRING PRIMARY KEY,      -- UUID
  profile_id BIGINT REFERENCES profile(profile_id),
  device_id STRING REFERENCES device(device_id),
  title_id BIGINT,
  episode_id BIGINT NULL,
  started_at TIMESTAMP,
  ended_at TIMESTAMP NULL
);

-- Append-only granular timeline
CREATE TABLE playback_event (
  session_id STRING,
  event_time TIMESTAMP,
  event_type STRING,              -- PLAY, PAUSE, SEEK, BITRATE_CHANGE, END, ERROR
  position_sec INT,               -- current playhead
  bitrate_kbps INT NULL,
  PRIMARY KEY (session_id, event_time)
);

-- Denormalized current resume pointer (updated by stream job)
CREATE TABLE resume_state (
  profile_id BIGINT,
  title_id BIGINT,
  episode_id BIGINT NULL,
  last_position_sec INT,
  last_update TIMESTAMP,
  PRIMARY KEY (profile_id, COALESCE(episode_id, title_id))
);
```

**Lakehouse**:

* `playback_event` **partition** by `dt=date(event_time)` and optionally `country_code`; **cluster** by `session_id`.
* `resume_state` small, unpartitioned; updated via incremental job from events.

**Continue Watching query**:

* Select top N from `resume_state` for a profile ordered by `last_update` desc.

**Trade-offs**:

* Store events append-only (immutable) → accurate replays; derive `resume_state` to serve fast UX.
