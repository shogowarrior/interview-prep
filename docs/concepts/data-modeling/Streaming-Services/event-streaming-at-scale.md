# Event Streaming @ scale (schema, processing, queryability)

**Ingestion design**:

* Kafka topics: `playback_events`, `app_events`, `billing_events`.
* **Schema Registry** with Avro/Protobuf for evolution (backward compatible).
* Keys:
  * `session_id` for `playback_events` (affinity ordering).
  * `profile_id` for `app_events`.
* Partitions sized to peak throughput; enable idempotent producers + exactly-once sinks (e.g., Spark Structured Streaming + Delta).

**Bronze/Silver/Gold**:

* **Bronze**: raw JSON/Avro → `dt` partition, no transforms.
* **Silver**: cleaned & typed; dedup on `(session_id, event_time)`; join dims (country, device).
* **Gold**: business aggregates (`resume_state`, `dau_by_region`, `qos_session_summary`).

**Storage formats**:

* **Delta/Iceberg** + Parquet; ZSTD or Snappy; optimize file sizes 128–512 MB.

**Queryability**:

* Precompute serving tables (resume, top-K recs).
* Enable ad-hoc via Trino/Spark; use clustering for high-selectivity keys.
