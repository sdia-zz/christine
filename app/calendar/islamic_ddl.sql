DROP TABLE IF EXISTS christine.calendar_islamic;
CREATE TABLE IF NOT EXISTS christine.calendar_islamic (
  isodate DATE PRIMARY KEY,
  year INT,
  month INT,
  day INT
);
