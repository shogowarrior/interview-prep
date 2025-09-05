# Partitioning & Sharding user watch history

**Goal**:

* Balance write load, avoid hot partitions, enable common queries.

**Choices**:

* **Partition column** (lake): `dt = DATE(event_time)`; maybe `region`.
* **Cluster/Bucket** (lake/warehouse): `profile_id` or `session_id` to collocate events.
* **OLTP sharding** (if needed):
  * Shard key = `account_id` or `profile_id` using consistent hashing.
  * **Pros of `profile_id`**: isolates heavy users; good affinity for per-profile queries.
  * **Pros of `account_id`**: easy household-level enforcement (device limits).
* **Hot keys**: VIPs or major launches → add **composite key** (`profile_id` + modulo/random salt) for write spreading; reassemble with map-side combine.
* **Skew management**: periodic **rebalancing** for shards with disproportionate size; use **auto-splitting** if supported.

**Examples**:

* Lake: `playback_event` → `PARTITION BY dt` and **CLUSTER BY (session\_id)**.
* Warehouse: **bucketing** `playback_event` by `profile_id` into, say, 256 buckets to speed joins with `profile` and rollups.

**Trade-offs**:

* Over-partitioning (`dt`, `hour`, `region`) → too many small files. Prefer `dt` + clustering; run optimize/compaction jobs.
* Using `profile_id` as shard key complicates account-level queries; mitigate via secondary indexes/materialized views.
  