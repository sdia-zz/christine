DROP TABLE IF EXISTS christine.calendar_bahai;
CREATE TABLE IF NOT EXISTS christine.calendar_bahai (
  isodate DATE PRIMARY KEY,
  year INT,
  month INT,
  day INT
);
