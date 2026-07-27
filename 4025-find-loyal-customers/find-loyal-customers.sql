# Write your MySQL query statement below

with data as (select customer_id,(case when min(transaction_date)<=DATE_SUB(max(transaction_date),INTERVAL 30 DAY) then 1 else 0 end) as value1,sum(case when transaction_type='purchase' then 1 else 0 end) as value2 ,sum(case when transaction_type='refund' then 1 else 0 end)/count(transaction_type) as value3 from customer_transactions  group by customer_id having value1=1 and value2>=3 and value3<0.2)
select customer_id from data