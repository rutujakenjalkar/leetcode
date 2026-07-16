# Write your MySQL query statement below

select user_id as buyer_id,join_date , sum(case when YEAR(order_date)=2019 then 1 else 0 end) as orders_in_2019 from Users left join Orders on Users.user_id=Orders.buyer_id   group by user_id