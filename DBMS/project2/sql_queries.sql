-- TODO: start<=end

-- insert new project and subprojects
insert into Projects 
Values
    ('Proj1', 'Espoo', '2020-04-17', '2020-05-12'),
    ('Proj2', 'Helsinki', '2020-03-09', '2020-04-10');

insert into Subprojects
Values
    ("SubProj 1", NULL, '2020-04-20', '2020-05-01', 'Proj1'),
    ("SubProj 2", "SubProj 1", '2020-04-23', '2020-04-29', 'Proj1');

-- Find out the current projects or the projects which were finished last year
select projectID from Projects where start<="2020-05-12" and finish>="2020-05-12";
select projectID from Projects where end>="2019-01-01" and finish<="2019-12-31";

-- Find subproject that must to completed before a "SubProj 2"
select prerequisiteID from Subprojects where subID="SubProj 2"

-- Qualifications needed for subproject  'SPR01-01':
select qualification from QualificationRequirements where subID='SPR01-01';

-- Assign a certain employee to a certain subproject.
-- Assuming an employee is assigned to a subporject for it's whole duration
insert into EmployeeAssignments
Values
    ('100584-163A', 'SubProj 1');


-- Find the machines needed in a certain subproject and the time periods they are needed.
select model, start, end , modelCount from MachineRequirements where subID='SPR01-02'

-- Find out which project a certain machine (item) is assigned to in a time period 2019-04-23 to 2019-
--  or in
-- which project it was last used.
select * from MachineAssignments where machineID='PD01' and start<=""



-- Find which machine is available at a certain time
select * from OwnedMachines where machineID not in (select machineID from MachineAssignments where start<="2020-05-12" and end>="2020-05-12")

-- Finding employees with a qualification who are available at a certain time
select Employees.ssn, name from Employees, HasQualification 
where 
    Employees.ssn=HasQualification.ssn 
    and qualification='worker' 
    and Employees.ssn not in (select ssn from EmployeeAssignments, Subprojects where EmployeeAssignments.subID=Subprojects.subID and start<='2019-03-10' and finish>='2019-03-09')

-- Finding which subprojects require a specific subproject to be completed
select subID from Subprojects where prerequisiteID='SPR01-01'

-- Finding out which subprojects are missing qualifications or have more than required qualifiactions assigned
select * from Subprojects 
where 
    /*required qualifications*/(select qualification, countOf from QualificationRequirements where subID=Subprojects.subID order by qualification) <>
    /*assigned qualifications*/(select qualification, count(*) from HasQualification where ssn in (select ssn from EmployeeAssignments where subID=Subprojects.subID) group by qualification order by qualification)


-- Find when a machine was last used and in which subproject and Project.
select min(end), subID, partOfproject from MachineAssignments as M, Subprojects as S
where machineID='PD01' and M.subID=S.subID