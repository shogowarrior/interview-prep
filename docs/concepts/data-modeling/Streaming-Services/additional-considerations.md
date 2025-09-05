## 11. Additional Considerations: Storage and Governance

These guardrails are essential for production data systems and frequently come up in interviews:

* **PII separation**: store PII (email, payment tokens) in a restricted table/key vault; reference by surrogate IDs.

* **Slowly Changing Dimensions**: use SCD2 for plans/regions to support point-in-time analytics.

* **Data quality**: contracts + expectations (e.g., Great Expectations/Deequ) with fail-open/closed strategy by table.

* **Backfills**: design idempotent jobs and partition filters; track backfill lineage.