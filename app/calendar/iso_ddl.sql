DROP TABLE IF EXISTS christine.calendar_iso;
CREATE TABLE IF NOT EXISTS christine.calendar_iso (
  isodate DATE PRIMARY KEY,
  year INT,
  week_number INT,
  weekday_number INT
);
