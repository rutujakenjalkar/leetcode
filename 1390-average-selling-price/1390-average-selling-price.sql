# Write your MySQL query statement below
select p.product_id, round(ifnull(sum(p.price * ifnull(u.units,0))/sum(u.units),0),2) as average_price 
from prices p 
left  join unitssold u 
on p.product_id=u.product_id 
where purchase_date is null or 
  ( purchase_date>=start_date and purchase_date<=end_date ) group by p.product_id