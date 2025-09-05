## 3) Recommendations storage (relationships & features)

**Layers**:

1. **Interactions**: views, ratings, thumbs, dwell time (from events).
2. **Similarity graph**: `item_item_edge` with score & model metadata.
3. **Personalized recs**: per-profile top-K lists per context (home row, genre row).
4. **Model lineage**: which model/version produced which list.

**DDL (analytics)**:

```sql
CREATE TABLE item_item_edge (
  src_title_id BIGINT,
  dst_title_id BIGINT,
  score DOUBLE,
  model VARCHAR,            -- e.g., 'itemCF', 'graphSage'
  model_version STRING,
  computed_at TIMESTAMP,
  PRIMARY KEY (src_title_id, dst_title_id, model, model_version)
);

CREATE TABLE personalized_recs (
  profile_id BIGINT,
  context STRING,           -- 'home', 'because_you_watched', 'kids'
  rank INT,
  title_id BIGINT,
  score DOUBLE,
  model STRING,
  model_version STRING,
  generated_at TIMESTAMP,
  PRIMARY KEY (profile_id, context, rank, generated_at)
);

CREATE TABLE feature_store_items (
  title_id BIGINT PRIMARY KEY,
  embedding VECTOR(256)     -- or store in a vector DB; here as opaque blob/bytes
);
```

**Serving**:

* Latest `personalized_recs` for `(profile_id, context)`; TTL and regeneration SLAs.
* For candidate gen on the fly: pull `item_item_edge` for last-watched titles.

**Trade-offs**:

* Precompute top-K for speed; keep edges for diversity/cold-start logic; store model lineage for A/B/debug.