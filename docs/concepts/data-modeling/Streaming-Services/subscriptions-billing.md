## 5) Subscriptions, Billing, Promotions, Payments

**Concepts**:

* Subscription *state machine* with effective-dated changes (SCD-2 style).
* Separate **invoice** and **payment** for accounting; support partials/refunds.

```sql
CREATE TABLE plan (
  plan_id STRING PRIMARY KEY,        -- 'STANDARD_ADS', 'PREMIUM'
  price_cents INT,
  currency STRING,
  max_screens INT,
  hdr BOOLEAN,
  ads_supported BOOLEAN
);

-- Effective-dated subscription records
CREATE TABLE subscription (
  subscription_id BIGINT PRIMARY KEY,
  account_id BIGINT,
  plan_id STRING REFERENCES plan(plan_id),
  status STRING,                     -- ACTIVE, PAUSED, CANCELED
  start_date DATE,
  end_date DATE NULL                 -- null = current
);

CREATE TABLE promotion (
  promo_code STRING PRIMARY KEY,
  discount_type STRING,              -- PCT or FIXED
  discount_value DOUBLE,
  start_date DATE,
  end_date DATE
);

CREATE TABLE subscription_event (
  event_id BIGINT PRIMARY KEY,
  subscription_id BIGINT REFERENCES subscription(subscription_id),
  event_time TIMESTAMP,
  event_type STRING,                 -- UPGRADE, DOWNGRADE, CANCEL, RESUME, RENEW
  old_plan_id STRING,
  new_plan_id STRING,
  note STRING
);

CREATE TABLE invoice (
  invoice_id BIGINT PRIMARY KEY,
  account_id BIGINT,
  period_start DATE,
  period_end DATE,
  amount_due_cents INT,
  currency STRING,
  promo_code STRING NULL REFERENCES promotion(promo_code),
  created_at TIMESTAMP,
  status STRING                      -- OPEN, PAID, VOID
);

CREATE TABLE payment (
  payment_id BIGINT PRIMARY KEY,
  invoice_id BIGINT REFERENCES invoice(invoice_id),
  amount_cents INT,
  currency STRING,
  method STRING,                     -- card, paypal, gift
  status STRING,                     -- AUTH, CAPTURED, REFUNDED, FAILED
  created_at TIMESTAMP
);
```

**Handling mid-cycle plan changes**:

* Emit `subscription_event` + proration logic in billing job: create a credit line on current invoice; new pro-rated charge line.