CREATE TABLE Students (
       ID TEXT PRIMARY KEY,
       name TEXT,
       program TEXT,
       year INTEGER
);

CREATE TABLE Courses (
       code TEXT PRIMARY KEY,
       name TEXT,
       credits REAL
);

CREATE TABLE Grades (
       studentID TEXT,
       courseCode TEXT,
       date TEXT,
       grade INTEGER,
       PRIMARY KEY (studentID, courseCode)
);


INSERT INTO Students
VALUES('112233', 'Teemu Teekkari', 'TIK', 2017);
INSERT INTO Students
VALUES('123456', 'Tiina Teekkari', 'TUO', 2019);
INSERT INTO Students
VALUES('224411', 'Maija Virtanen', 'AUT', 2018);

INSERT INTO Courses
VALUES('CS-A1111', 'Basic Course in Programming Y1', 5.0);
INSERT INTO Courses
VALUES('CS-A1120', 'Programming 2', 5.0);

INSERT INTO Grades
VALUES('112233', 'CS-A1111', '2017-12-05', 3);
INSERT INTO Grades
VALUES('112233', 'CS-A1120', '2018-12-19', 1);
INSERT INTO Grades
VALUES('224411', 'CS-A1111', '2018-12-12', 4);
