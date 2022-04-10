SELECT 
A.first_name, A.last_name, C.list_price*C.quantity as price  from 
sale.customer A ,sale.orders B, sale.order_item C  WHERE A.customer_id=B.customer_id
AND B.order_id=C.order_id
AND C.list_price*C.quantity <(SELECT C.list_price*C.quantity  from 
sale.customer A ,sale.orders B, sale.order_item C  WHERE A.customer_id=B.customer_id
AND B.order_id=C.order_id
AND first_name='Richard' AND last_name='Perin')
GROUP BY A.first_name, A.last_name, C.list_price*C.quantity 
order by C.list_price*C.quantity desc
--------------------------------------------------------------------------
SELECT 
A.first_name, A.last_name, SUM(C.list_price*C.quantity) as price  from 
sale.customer A ,sale.orders B, sale.order_item C  WHERE A.customer_id=B.customer_id
AND B.order_id=C.order_id

GROUP BY A.first_name, A.last_name

HAVING  SUM(C.list_price*C.quantity) <(SELECT C.list_price*C.quantity  from 
sale.customer A ,sale.orders B, sale.order_item C  WHERE A.customer_id=B.customer_id
AND B.order_id=C.order_id
AND first_name='Richard' AND last_name='Perin')
order by SUM(C.list_price*C.quantity) desc
------------------------------------------------------------------------

SELECT *, CASE
              WHEN order_date=shipped_date THEN 'Fast'
			  WHEN DATEDIFF(day,order_date,shipped_date) >= 3 THEN 'Slow'
			  WHEN DATEDIFF(day,order_date,shipped_date) IN (1,2) THEN 'Normal'
			  ELSE 'Not Shipped'
			  END as ORDER_LABEL
FROM sale.orders
order by shipped_date


---------------------------------------------------------------
USE SampleRetail

CREATE TABLE Actions (
	Visitor_ID int IDENTITY(1,1) NOT NULL PRIMARY KEY,
	Adv_Type nchar(10) NOT NULL,
	Action nchar(10) NOT NULL)

select Adv_Type,CAST(SUM(
      CASE 
	     WHEN Action='Order' THEN 1.0 ELSE 0.0
	   END)/ COUNT(Action) as DECIMAL(3,2))as Conversion_Rate
from Actions  
group by Adv_Type


--------------------------------------------------------------------

