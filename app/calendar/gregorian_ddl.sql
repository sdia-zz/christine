DROP TABLE IF EXISTS christine.calendar_gregorian;
CREATE TABLE IF NOT EXISTS christine.calendar_gregorian (
  isodate DATE PRIMARY KEY,
  year INT,
  month INT,
  day INT
);
