# Write your MySQL query statement below
SELECT A.Name AS Employee FROM Employee A, Employee B WHERE A.Salary > B.Salary AND A.ManagerId = B.Id;
