# Write your MySQL query statement below
select distinct(customer_id),count(*) as count_no_trans from Visits LEFT JOIN Transactions ON
Visits.visit_id=Transactions.visit_id where transaction_id is null group by customer_id ;