


SELECT DISTINCT X.customer_id,X.first_name,X.last_name,
ISNULL(NULLIF(ISNULL(STR(V.order_id),'No'),STR(V.order_id)),'Yes') First_product,
ISNULL(NULLIF(ISNULL(STR(Y.order_id),'No'),STR(Y.order_id)),'Yes') Second_product,
ISNULL(NULLIF(ISNULL(STR(Z.order_id),'No'),STR(Z.order_id)),'Yes') Third_product
FROM
(
SELECT D.customer_id,D.first_name,D.last_name,B.order_id
FROM product.product A, sale.order_item B,sale.orders C, sale.customer D
WHERE A.product_id=B.product_id
AND B.order_id=C.order_id
AND C.customer_id=D.customer_id
AND A.product_id=6
) X
LEFT JOIN
(
SELECT D.customer_id,D.first_name,D.last_name,B.order_id
FROM product.product A, sale.order_item B,sale.orders C, sale.customer D
WHERE A.product_id=B.product_id
AND B.order_id=C.order_id
AND C.customer_id=D.customer_id
AND A.product_id=13
) V
ON V.customer_id =X.customer_id
LEFT JOIN
(
SELECT D.customer_id,D.first_name,D.last_name,B.order_id
FROM product.product A, sale.order_item B,sale.orders C, sale.customer D
WHERE A.product_id=B.product_id
AND B.order_id=C.order_id
AND C.customer_id=D.customer_id
AND A.product_id=21
) Y

ON X.customer_id=Y.customer_id

LEFT JOIN
(
SELECT D.customer_id,D.first_name,D.last_name,B.order_id
FROM product.product A, sale.order_item B,sale.orders C, sale.customer D
WHERE A.product_id=B.product_id
AND B.order_id=C.order_id
AND C.customer_id=D.customer_id
AND A.product_id=16
) Z

ON X.customer_id=Z.customer_id

Order By X.customer_id






















FROM (SELECT customer.customer_id,product.product_id
FROM sale.customer 




LEFT JOIN sale.orders ON customer.customer_id=orders.customer_id 
LEFT JOIN product.stock ON stock.store_id=orders.store_id
AND product.product ON product.product_id=stock.product_id



SELECT DISTINCT A.customer_id, A.first_name, A.last_name, D.product_id, (SELECT ISNULL(NULLIF('NO ', ISNULL(NULLIF(D.product_name, 'Polk Audio - 50 W Woofer - Black'), 'NO ')), 'YES'))  AS First_product,(SELECT ISNULL(NULLIF('NO ', ISNULL(NULLIF(D.product_name, 'SB-2000 12 500W Subwoofer (Piano Gloss Black)'), 'NO ')), 'YES'))  AS Second_product,(SELECT ISNULL(NULLIF('NO ', ISNULL(NULLIF(D.product_name,  'Virtually Invisible 891 In-Wall Speakers (Pair)'), 'NO ')), 'YES')) AS Third_productFROM sale.customer ALEFT JOIN sale.orders BON A.customer_id = B.customer_idLEFT JOIN sale.order_item CON B.order_id = C.order_idLEFT JOIN product.product DON C.product_id = D.product_id WHERE D.product_id = 13 or D.product_id = 21 or D.product_id = 16ORDER BY A.customer_id
