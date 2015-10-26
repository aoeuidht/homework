/*
Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

*/

-- create table with
/*
create table Employee (
 id int primary key AUTO_INCREMENT,
 salary int not null default 0);
*/

drop function getNthHighestSalary ;
DELIMITER //

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  return (select b.Salary from Employee as a left join Employee as b on a.Salary > b.Salary where a.id = (select id from Employee order by Salary desc limit 1) order by b.Salary desc limit 1 offset N-1);
END; //
DELIMITER ;


select getNthHighestSalary(2);
