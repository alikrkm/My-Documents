create view xtable asSELECT product_id,count(quantity) count_quantity_2 ,AVG(discount) avg_discount_2from sale.order_itemWhere quantity IN(2)group by product_id create view ytable asSELECT product_id,count(quantity) count_quantity_1,AVG(discount) avg_discount_1from sale.order_item BWhere quantity IN(1)group by product_idSELECT distinct order_item.product_id, CASE                                   WHEN count_quantity_2 > count_quantity_1 AND avg_discount_2 >= avg_discount_1  THEN  'Positive'                          WHEN count_quantity_2 > count_quantity_1 AND avg_discount_2 < avg_discount_1  THEN  'Negative'						  WHEN count_quantity_2 < count_quantity_1 AND avg_discount_2 < avg_discount_1  THEN  'Positive'						  WHEN count_quantity_2 < count_quantity_1 AND avg_discount_2 >= avg_discount_1  THEN  'Negative'						  ELSE 'Neutral'				          END as Discount_EffectFROM sale.order_item FULL OUTER JOIN xtableON order_item.product_id=xtable.product_id FULL OUTER JOIN ytableON order_item.product_id=ytable.product_idgroup by order_item.product_id, CASE                                   WHEN count_quantity_2 > count_quantity_1 AND avg_discount_2 >= avg_discount_1  THEN  'Positive'                          WHEN count_quantity_2 > count_quantity_1 AND avg_discount_2 < avg_discount_1  THEN  'Negative'						  WHEN count_quantity_2 < count_quantity_1 AND avg_discount_2 < avg_discount_1  THEN  'Positive'						  WHEN count_quantity_2 < count_quantity_1 AND avg_discount_2 >= avg_discount_1  THEN  'Negative'						  ELSE 'Neutral'				          END						  order by order_item.product_id