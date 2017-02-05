DROP TABLE IF EXISTS christine.calendar_positivist;
CREATE TABLE IF NOT EXISTS christine.calendar_positivist (
  isodate DATE PRIMARY KEY,
  year INT,
  month INT,
  day INT
);
