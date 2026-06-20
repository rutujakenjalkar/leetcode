# Write your MySQL query statement below

WITH RANKED_EMPLOYEES AS
(select
 Department.name as Department,Employee.name as Employee ,
  DENSE_RANK() OVER ( PARTITION BY Employee.DepartmentId ORDER BY Employee.salary DESC) AS Salary_rank,Employee.salary as Salary
  from Employee join Department on Employee.departmentId=Department.id)
select Department,Employee, Salary from RANKED_EMPLOYEES where Salary_rank<=3;