# Write your MySQL query statement below
select name as NAME,sum(amount) as BALANCE  from Users join Transactions on Users.account=Transactions.account group by name having BALANCE>10000