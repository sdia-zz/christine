DROP schema IF EXISTS christine CASCADE;
CREATE schema christine;


--------------------------------------------------------------------------------
-- christine.wikipedia_raw
--------------------------------------------------------------------------------
DROP TABLE IF EXISTS christine.wikipedia_raw;
CREATE TABLE christine.wikipedia_raw(
  inserted_at TIMESTAMP WITHOUT TIME ZONE DEFAULT (now() AT TIME ZONE 'utc'),
  event_date DATE,
  event_raw TEXT
  -- , PRIMARY KEY(event_date)
);

CREATE INDEX ON christine.wikipedia_raw (event_date);


--------------------------------------------------------------------------------
-- christine.wikipedia_parsed
--------------------------------------------------------------------------------
DROP TABLE IF EXISTS christine.wikipedia_parsed;
CREATE TABLE christine.wikipedia_parsed(
  inserted_at TIMESTAMP WITHOUT TIME ZONE DEFAULT (now() AT TIME ZONE 'utc'),
  event_date DATE,
  event_type TEXT,
  event_title TEXT,
  event_body TEXT,
  event_sources TEXT[]
  -- , PRIMARY KEY(event_date, event_type)
);

CREATE INDEX ON christine.wikipedia_parsed (event_date);
CREATE INDEX ON christine.wikipedia_parsed (event_type);

DROP TABLE IF EXISTS christine.wikipedia_parsed_stg;
CREATE TABLE christine.wikipedia_parsed_stg (LIKE christine.wikipedia_parsed INCLUDING ALL);
