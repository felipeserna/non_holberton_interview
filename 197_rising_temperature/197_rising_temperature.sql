# Write your MySQL query statement below
SELECT A.Id FROM Weather A, Weather B
WHERE DATE_ADD(B.RecordDate, INTERVAL 1 DAY) = A.RecordDate AND A.Temperature > B.Temperature;
