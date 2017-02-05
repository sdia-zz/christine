DROP TABLE IF EXISTS christine.calendar_indian_civil;
CREATE TABLE IF NOT EXISTS christine.calendar_indian_civil (
  isodate DATE PRIMARY KEY,
  year INT,
  month INT,
  day INT
);
