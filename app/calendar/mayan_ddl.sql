DROP TABLE IF EXISTS christine.calendar_mayan;
CREATE TABLE IF NOT EXISTS christine.calendar_mayan (
  isodate DATE PRIMARY KEY,
  baktun INT,
  katun INT,
  tun INT,
  uinal INT,
  kin INT
);
