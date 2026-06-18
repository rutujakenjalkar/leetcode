# Write your MySQL query statement below

 SELECT 
    ROUND(((SELECT COUNT(order_date) 
      FROM Delivery 
      WHERE order_date = customer_pref_delivery_date 
        AND (customer_id, order_date) IN (
            SELECT customer_id, MIN(order_date) 
            FROM Delivery 
            GROUP BY customer_id
        )
     )
     /
     (SELECT COUNT(*) 
      FROM Delivery 
      WHERE (customer_id, order_date) IN (
          SELECT customer_id, MIN(order_date) 
          FROM Delivery 
          GROUP BY customer_id
      )
     )
    ) * 100,2) AS immediate_percentage;

