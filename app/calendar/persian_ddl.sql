DROP TABLE IF EXISTS christine.calendar_persian;
CREATE TABLE IF NOT EXISTS christine.calendar_persian (
  isodate DATE PRIMARY KEY,
  year INT,
  month INT,
  day INT
);
