# Write your MySQL query statement below



with data as
(select *,concat(lat," ",lon)  from Insurance where tiv_2015 in (select tiv_2015 from Insurance group by tiv_2015 having count(tiv_2015)>1) and concat(lat," ",lon) in (select concat(lat," ",lon) as loc  from Insurance group by loc having count(loc)=1))
select ROUND(sum(tiv_2016),2) as tiv_2016 from data














