# Write your MySQL query statement below

WITH data AS (
    SELECT 
        product_id,
        DENSE_RANK() OVER(PARTITION BY product_id ORDER BY change_date DESC) AS col, 
        change_date,
        new_price 
    FROM Products 
    WHERE change_date <= '2019-08-16'
),
LatestPrices AS (
    SELECT product_id, new_price AS price 
    FROM data 
    WHERE col = 1
)
SELECT DISTINCT P.product_id , case
    when L.price is null then 10 
    else L.price 
    end as price
FROM Products P
LEFT JOIN LatestPrices L 
    ON P.product_id = L.product_id;
