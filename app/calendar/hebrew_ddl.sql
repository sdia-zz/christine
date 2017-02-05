DROP TABLE IF EXISTS christine.calendar_hebrew;
CREATE TABLE IF NOT EXISTS christine.calendar_hebrew (
  isodate DATE PRIMARY KEY,
  year INT,
  month INT,
  day INT
);
