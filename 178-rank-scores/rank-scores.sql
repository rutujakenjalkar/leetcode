# Write your MySQL query statement below
with data as
(select score, dense_rank() over (order by score desc) as ran from Scores)
select score , ran as 'rank' from data;
