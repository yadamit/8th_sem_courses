SELECT * FROM Employees;


SELECT DISTINCT location FROM Projects;


SELECT subID FROM Subprojects 
WHERE START <= DATE("now") AND finish >= DATE("now"); 


SELECT subID, start, finish FROM Subprojects 
WHERE partOfProject = "PR01" ORDER BY start;


SELECT subID, start, finish FROM Subprojects 
WHERE start >= "2019-02-01" AND finish <= "2019-10-01" ORDER BY start;


SELECT subID FROM Subprojects WHERE prerequisiteID = "SPR01-01";


SELECT ssn, name FROM Employees, EmployeeAssignments
WHERE EmployeeAssignments.ssn = Employees.ssn AND subID = "SPR01-01";


SELECT OwnedMachines.machineID, model, start, end
FROM MachineAssignments, OwnedMachines
WHERE OwnedMachines.machineID = MachineAssignments.machineID
AND subID = "SPR01-01";


SELECT start, end, name FROM Absences, Employees 
WHERE absentSSN = "240383-107M" AND subSSN = ssn;


SELECT partOfProject FROM Subprojects, EmployeeAssignments 
WHERE EmployeeAssignments.subID = Subprojects.subID AND ssn = "210264-14H"; 


SELECT machineID, model
FROM OwnedMachines WHERE machineID NOT IN (
SELECT OwnedMachines.machineID 
FROM OwnedMachines, MachineAssignments, Maintenance
WHERE OwnedMachines.machineID = MachineAssignments.machineID
AND OwnedMachines.machineID = Maintenance.machineID
AND (
MachineAssignments.start < "2019-04-25" 
OR Maintenance.start < "2019-04-25"
)
AND (
MachineAssignments.end > "2019-04-25" 
OR Maintenance.end > "2019-04-25"
)
);


SELECT ssn, name, qualification FROM Employees, HasQualification
WHERE Employees.ssn = HasQualification.ssn
AND qualification = "worker"
AND Employees.ssn NOT IN (
SELECT ssn FROM EmployeeAssignments, Subprojects
WHERE EmployeeAssignments.subID = Subprojects.subID
AND start <= "2019-03-10" AND finish >= "2019-03-10"
)
AND Employees.ssn NOT IN (
SELECT absentSSN FROM Absences
WHERE start <= "2019-03-10" AND end >= "2019-03-10"
);


SELECT qualification, count(*) FROM HasQualification
WHERE ssn in 
(SELECT ssn FROM EmployeeAssignments WHERE subID='SPR01-01')
GROUP BY qualification;


SELECT qualification, countOf FROM QualificationRequirements 
WHERE subID='SPR01-01' ;


--should fail
INSERT INTO HasQualification
VALUES
('100000-000A', 'carpenter');


--should fail
INSERT INTO OwnedMachines
VALUES
('PD03', 'PK-000-A');


--should fail
UPDATE Subprojects
SET partOfProject = "NEWPROJECT"
WHERE subID = "SPR01-01";


--should fail
UPDATE Absences
SET end = NULL
WHERE absentSSN = "240383-107M"
AND start = "2019-03-12";


--should work
UPDATE Absences
SET end = "2019-04-01"
WHERE absentSSN = "240383-107M"
AND start = "2019-03-12";


SELECT min(end), subID, partOfproject 
FROM MachineAssignments as M, Subprojects as S
WHERE machineID='PD01' and M.subID=S.subID;