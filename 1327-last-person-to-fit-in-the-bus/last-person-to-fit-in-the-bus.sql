# Write your MySQL query statement below
with data as 
(select turn as Turn,turn as turn1, person_id,person_name ,Weight,
(select sum(weight) from Queue where turn1>=Turn) as rutuja
from Queue order by Turn)
select person_name from data where rutuja<=1000 order by rutuja desc limit 1
