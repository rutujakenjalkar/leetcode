# Write your MySQL query statement below
 with sales as (select Sales.product_id,Sales.sale_date,DENSE_RANK() over (partition by Sales.product_id order by Sales.sale_date) as date_rank,Product.product_name from Product join Sales where Product.product_id=Sales.product_id )
select product_id,product_name from sales group by product_id,product_name 
having min(sale_date)>='2019-01-01' and max(sale_date)<='2019-03-31'
