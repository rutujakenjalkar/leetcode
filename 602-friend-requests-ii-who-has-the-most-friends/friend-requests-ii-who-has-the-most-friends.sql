# Write your MySQL query statement below

with data as 
(select requester_id as id  from RequestAccepted 
UNION ALL
select accepter_id from RequestAccepted)
select id ,count(*) as num from data group by id order by count(*) desc limit 1

