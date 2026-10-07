-- 16

CREATE TABLE students (
  student_id INTEGER PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  email TEXT UNIQUE
);

CREATE TABLE teachers (
  teacher_id INTEGER PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL
);

CREATE TABLE instruments (
  instrument_id INTEGER PRIMARY KEY,
  name TEXT NOT NULL UNIQUE
);

CREATE TABLE teacher_instruments (
  teacher_id INTEGER NOT NULL,
  instrument_id INTEGER NOT NULL,
  PRIMARY KEY (teacher_id, instrument_id),
  FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
  FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id)
);

CREATE TABLE rooms (
  room_id INTEGER PRIMARY KEY,
  description TEXT
);

CREATE TABLE lessons (
  lesson_id INTEGER PRIMARY KEY,
  student_id INTEGER NOT NULL,
  teacher_id INTEGER NOT NULL,
  instrument_id INTEGER NOT NULL,
  room_id INTEGER NOT NULL,
  lesson_date TEXT NOT NULL,
  start_time TEXT NOT NULL,
  UNIQUE (room_id, lesson_date, start_time),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (teacher_id) REFERENCES teachers (teacher_id),
  FOREIGN KEY (instrument_id) REFERENCES instruments (instrument_id),
  FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);
