/*
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the second highest salary is 200. If there is no second highest salary, then the query should return null.

*/

-- test with this table
/*
create table Employee (
 id int primary key,
 salary int not null default 0);
*/

select max(b.Salary) as SecondHighestSalary from Employee as a left join Employee as b on a.Salary > b.Salary where a.id = (select id from Employee order by Salary desc limit 1);
