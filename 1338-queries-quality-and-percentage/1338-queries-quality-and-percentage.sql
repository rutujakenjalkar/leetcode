# Write your MySQL query statement below
select query_name,ROUND(sum(rating/position)/count(*),2) as quality,Round(avg(rating<3)*100,2) as poor_query_percentage from Queries group by query_name; 