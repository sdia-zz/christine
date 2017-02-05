DROP TABLE IF EXISTS christine.calendar_iso;
CREATE TABLE IF NOT EXISTS christine.calendar_iso (
  isodate DATE PRIMARY KEY,
  year INT,
  month INT,
  day INT
);
