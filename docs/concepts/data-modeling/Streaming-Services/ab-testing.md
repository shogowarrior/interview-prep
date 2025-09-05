## 7) A/B Testing (experiments, assignments, outcomes)

```sql
CREATE TABLE experiment (
  exp_id STRING PRIMARY KEY,
  name STRING,
  start_time TIMESTAMP,
  end_time TIMESTAMP,
  unit STRING,                    -- PROFILE or ACCOUNT
  primary_kpi STRING              -- e.g., 7d hours watched
);

CREATE TABLE variant (
  exp_id STRING REFERENCES experiment(exp_id),
  variant_id STRING,              -- 'control','treatment_a'
  traffic_pct DOUBLE,
  PRIMARY KEY (exp_id, variant_id)
);

CREATE TABLE assignment (
  exp_id STRING,
  unit_id STRING,                 -- profile_id or account_id as text
  variant_id STRING,
  assigned_at TIMESTAMP,
  PRIMARY KEY (exp_id, unit_id)
) PARTITIONED BY (exp_id);

-- Outcomes joined from facts (watch hours, conversions, etc.)
CREATE TABLE kpi_outcome (
  exp_id STRING,
  unit_id STRING,
  metric_date DATE,
  kpi_name STRING,                -- 'watch_hours', 'retention_d30'
  kpi_value DOUBLE,
  PRIMARY KEY (exp_id, unit_id, metric_date, kpi_name)
);
```

**Analysis**:

* Guardrails: compare pre-period covariates; use CUPED or stratification.
* Avoid contamination: unit = `profile` for recs; `account` for pricing.