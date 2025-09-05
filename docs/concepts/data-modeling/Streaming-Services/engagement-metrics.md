# Engagement Metrics (DAU by region)

**Ingest**:

* Client/app pings → `app_event` (login, foreground, heartbeat) with `profile_id`, `region`, `event_time`.

**Lakehouse table**:

```sql
CREATE TABLE app_event (
  profile_id BIGINT,
  account_id BIGINT,
  region STRING,                      -- e.g., US, BR, IN
  event_name STRING,
  event_time TIMESTAMP
) PARTITIONED BY (dt DATE)            -- dt = DATE(event_time)
CLUSTER BY (region, profile_id);
```

**Metric build**:

```sql
-- DAU per region (distinct profiles with any event)
CREATE OR REPLACE VIEW dau_by_region AS
SELECT
  dt,
  region,
  COUNT(DISTINCT profile_id) AS dau
FROM app_event
GROUP BY dt, region;
```

**Notes**:

* Use incremental processing per `dt`; compact small files; Z-Order/cluster by `region` if supported.
