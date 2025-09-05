## 4) Accounts, Profiles, Devices

```sql
CREATE TABLE account (
  account_id BIGINT PRIMARY KEY,
  created_at TIMESTAMP,
  home_country STRING,
  billing_currency STRING
);

CREATE TABLE profile (
  profile_id BIGINT PRIMARY KEY,
  account_id BIGINT REFERENCES account(account_id),
  name STRING,
  is_kids BOOLEAN,
  language_pref STRING,
  created_at TIMESTAMP
);

CREATE TABLE device (
  device_id STRING PRIMARY KEY,
  account_id BIGINT REFERENCES account(account_id),
  device_type STRING,
  registered_at TIMESTAMP
);

CREATE TABLE profile_device_link (
  profile_id BIGINT REFERENCES profile(profile_id),
  device_id STRING REFERENCES device(device_id),
  PRIMARY KEY (profile_id, device_id)
);
```

**Notes**:

* Device belongs to account; link to profiles many-to-many for usage/permissions.
* Enforce device limits via a separate `active_streams` store or cache keyed by `account_id`.