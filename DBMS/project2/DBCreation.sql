CREATE TABLE Projects (
projectID TEXT PRIMARY KEY,
location TEXT,
start TEXT,
finish TEXT
);


CREATE TABLE Subprojects (
subID TEXT PRIMARY KEY,
prerequisiteID TEXT REFERENCES Subprojects(subID),
start TEXT,
finish TEXT,
partOfProject TEXT REFERENCES Projects(projectID)
);


CREATE TABLE Employees (
ssn TEXT PRIMARY KEY,
name TEXT NOT NULL
);


CREATE TABLE Qualifications (
qualification TEXT PRIMARY KEY
);


CREATE TABLE HasQualification (
ssn TEXT REFERENCES Employees(ssn),
qualification TEXT REFERENCES Qualifications(qualification),
PRIMARY KEY (ssn, qualification)
);


CREATE TABLE QualificationRequirements (
qualification TEXT REFERENCES Qualifications(qualification),
subID TEXT REFERENCES Subprojects(subID),
countOf INTEGER,
PRIMARY KEY (qualification, subID)
);


CREATE TABLE Absences (
absentSSN TEXT REFERENCES Employees(ssn),
start TEXT,
end TEXT NOT NULL,
subSSN TEXT REFERENCES Employees(ssn),
PRIMARY KEY (AbsentSSN, start)
);


CREATE TABLE EmployeeAssignments (
ssn TEXT REFERENCES Employees(ssn),
subID TEXT REFERENCES Subprojects(subID),
PRIMARY KEY (ssn, subID)
);


CREATE TABLE Machines (
model TEXT PRIMARY KEY,
manufacturer TEXT,
description TEXT,
size INTEGER,
fuelConsumption INTEGER
);


CREATE TABLE OwnedMachines (
machineID TEXT PRIMARY KEY,
model TEXT REFERENCES Machines(model)
);


CREATE TABLE Maintenance (
machineID TEXT REFERENCES OwnedMachines(machineID),
start TEXT,
end TEXT,
PRIMARY KEY (machineID, start)
);


CREATE TABLE MachineAssignments (
machineID TEXT REFERENCES OwnedMachines(machineID),
start TEXT,
end TEXT,
subID TEXT REFERENCES Subprojects(subID),
PRIMARY KEY(machineID, start)
);


CREATE TABLE MachineRequirements (
model REFERENCES Machines(model),
start TEXT,
subID TEXT REFERENCES Subprojects(subID),
end TEXT,
modelCount INTEGER,
PRIMARY KEY (model, start, subID)
);


CREATE INDEX ProjectIndex ON Projects(projectID);
CREATE INDEX SubprojectIndex ON Subprojects(subID);
CREATE INDEX EmployeeIndex ON Employees(ssn);
CREATE INDEX MachineIndex ON Machines(model);
CREATE INDEX OwnedIndex ON OwnedMachines(machineID);
CREATE INDEX EmployeeWorkedAt ON EmployeeAssignments(ssn);


CREATE VIEW AvailableEmployees AS
        SELECT Employees.ssn, Employees.name, HasQualification.qualification
        FROM Employees, HasQualification
        WHERE Employees.ssn = HasQualification.ssn
        EXCEPT
        SELECT Employees.ssn, Employees.name, HasQualification.qualification
        FROM Employees, HasQualification, EmployeeAssignments, Absences
        WHERE Employees.ssn = HasQualification.ssn AND Employees.ssn = 
(SELECT EmployeeAssignments.ssn
FROM EmployeeAssignments, Subprojects
WHERE EmployeeAssignments.subID = Subprojects.subID AND start <= date('now') AND finish >= date('now')
) OR Employees.ssn = 
(SELECT absentSSN
FROM Absences
WHERE start <= date('now') AND end >= date('now')
);


INSERT INTO Projects 
VALUES ('PR01','Espoo', '2019-03-09', '2020-05-24');


INSERT INTO Subprojects
VALUES
('SPR01-01', NULL, '2019-03-09', '2019-04-20', 'PR01'),
('SPR01-02', 'SPR01-01', '2019-04-20', '2020-05-24', 'PR01');


INSERT INTO Employees
VALUES
('100584-163A', 'Lauri Loronen'),
('210264-14H', 'Pasi Sorjonen'),
('240383-107M', 'Pasi Rantanen'),
('190892-113I', 'Jaakko Virtanen'),
('040686-034K', 'Vadim Oblist'),
('081091-141L', 'Joona Silanen');


INSERT INTO Qualifications
VALUES
('designer'),
('supervisor'),
('worker'),
('caster'),
('carpenter');


INSERT INTO HasQualification
VALUES
('100584-163A', 'designer'),
('210264-14H', 'supervisor'),
('240383-107M', 'worker'),
('190892-113I', 'worker'),
('040686-034K', 'worker'),
('081091-141L', 'worker'),
('081091-141L', 'caster');


INSERT INTO QualificationRequirements
VALUES
('designer', 'SPR01-01', 1),
('supervisor', 'SPR01-01', 1),
('worker', 'SPR01-01', '3');


INSERT INTO Absences 
VALUES ('240383-107M', '2019-03-12', '2019-03-15', '040686-034K');


INSERT INTO EmployeeAssignments
VALUES
('100584-163A', 'SPR01-01'),
('210264-14H', 'SPR01-01'),
('240383-107M', 'SPR01-01'),
('190892-113I', 'SPR01-01'),
('081091-141L', 'SPR01-01');


INSERT INTO Machines
VALUES
        ('PK-130-F', 'BOSCH', 'Power drill', 130, 55),
        ('RD180-M', 'Faust', 'Grinder', 180, 40),
        ('JD Devastator 250', 'John Deer', 'Bulldozer', 250, 135);


INSERT INTO OwnedMachines
VALUES
        ('PD01', 'PK-130-F'),
        ('PD02', 'PK-130-F'),
        ('BD01', 'JD Devastator 250');


INSERT INTO Maintenance
VALUES ('PD01', '2018-07-15', '2018-07-17');


INSERT INTO MachineAssignments
VALUES
('PD01', '2019-04-20', '2019-04-30', 'SPR01-02'),
('PD02', '2019-04-30', '2019-05-15', 'SPR01-02'),
('BD01', '2019-03-09', '2019-04-10', 'SPR01-01');




INSERT INTO MachineRequirements
VALUES
        ('JD Devastator 250', '2019-03-09', 'SPR01-01', '2019-04-10', 1),
        ('PK-130-F', '2019-04-20', 'SPR01-02', '2019-04-30', '1'),
        ('PK-130-F', '2019-04-30', 'SPR01-02', '2019-05-15', '1');