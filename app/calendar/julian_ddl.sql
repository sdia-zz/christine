DROP TABLE IF EXISTS christine.calendar_julian;
CREATE TABLE IF NOT EXISTS christine.calendar_julian (
  isodate DATE PRIMARY KEY,
  year INT,
  month INT,
  day INT
);
