## 1) Content Catalog (titles, seasons, episodes, genres, localization)

**Core entities**:

* `title` (movie or show), `season`, `episode`, `genre`, many-to-many `title_genre`
* Localization stored separately per locale.

**Relational-ish DDL**:

```sql
-- Type can be MOVIE or SHOW
CREATE TABLE title (
  title_id BIGINT PRIMARY KEY,
  type STRING NOT NULL,
  release_date DATE,
  maturity_rating STRING,
  production_country STRING,
  is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE season (
  season_id BIGINT PRIMARY KEY,
  title_id BIGINT NOT NULL REFERENCES title(title_id),
  season_number INT NOT NULL,
  UNIQUE(title_id, season_number)
);

CREATE TABLE episode (
  episode_id BIGINT PRIMARY KEY,
  title_id BIGINT NOT NULL REFERENCES title(title_id),
  season_id BIGINT REFERENCES season(season_id),
  episode_number INT,
  duration_sec INT,
  UNIQUE(title_id, season_id, episode_number)
);

CREATE TABLE genre (
  genre_id INT PRIMARY KEY,
  name STRING UNIQUE
);

CREATE TABLE title_genre (
  title_id BIGINT REFERENCES title(title_id),
  genre_id INT REFERENCES genre(genre_id),
  PRIMARY KEY (title_id, genre_id)
);

-- Localization (can apply to titles, seasons, or episodes)
CREATE TABLE localized_metadata (
  object_type STRING CHECK (object_type IN ('TITLE','SEASON','EPISODE')),
  object_id BIGINT,
  locale STRING,                      -- e.g., en-US, es-MX
  localized_title STRING,
  localized_description STRING,
  PRIMARY KEY (object_type, object_id, locale)
);
```

**Lakehouse layout**:

* Tables in Delta/Iceberg; **partition** `title` sparsely (usually not necessary).
* For big read throughput on `episode`, consider **clustering/bucketing** by `title_id`.
* `localized_metadata` clustered by `(object_type, object_id)`; filter by `locale`.

**Queries**:

* Get all episodes of S2 for a show: filter `title_id` + `season_number=2`, join `episode`.
* Localized listing: join `localized_metadata` on requested `locale`, fallback to `en-US`.

**Trade-offs**:

* Keep movies and shows unified in `title` to simplify cross-type queries.
* Localization separated avoids column bloat and supports sparse locales.