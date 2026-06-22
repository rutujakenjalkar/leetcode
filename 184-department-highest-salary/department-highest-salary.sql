# Write your MySQL query statement below
WITH RANKED_EMPLOYEES AS (
    SELECT DEPARTMENT.name as Department , EMPLOYEE.name as Employee ,Employee.salary as Salary ,
    DENSE_RANK() OVER (Partition by Employee.departmentId ORDER BY Employee.salary DESC) as salary_rank from Employee join Department on
     Employee.departmentID= Department.id
) select Department,Employee,Salary from RANKED_EMPLOYEES where salary_rank=1;
