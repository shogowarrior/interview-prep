## 8) Streaming Quality (bitrate, buffering, errors)

**Granular**:

* Use `playback_event` (from #2) with QoS fields; or a dedicated QoS topic/table.

```sql
CREATE TABLE qos_event (
  session_id STRING,
  event_time TIMESTAMP,
  q_event STRING,                 -- STARTUP, BUFFERING_START, BUFFERING_END, BITRATE_CHANGE, ERROR
  position_sec INT,
  bitrate_kbps INT,
  cdn STRING,
  error_code STRING NULL,
  PRIMARY KEY (session_id, event_time)
) PARTITIONED BY (dt DATE);
```

**Rollups**:

```sql
-- Per session QoS summary
CREATE TABLE qos_session_summary AS
SELECT
  session_id,
  MIN(event_time) AS start_time,
  MAX(event_time) AS end_time,
  SUM(CASE WHEN q_event='BUFFERING_START' THEN 1 ELSE 0 END) AS rebuffer_count,
  SUM(rebuffer_duration_sec) AS rebuffer_time_sec,   -- computed via pairing START/END
  AVG(bitrate_kbps) AS avg_bitrate
FROM transform_qos_events(/* window/pairs */)
GROUP BY session_id;
```

**Use**:

* Monitor `rebuffer_ratio = rebuffer_time / session_time` by device/region/CDN.