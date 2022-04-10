



						 -- DAwSQL Oturumu -8

-- E-Ticaret Projesi Çözümü



-- 1. Tüm tablolara katılın ve birleştirilmiş_tablo adında yeni bir tablo oluşturun. (market_fact, cust_dimen, order_dimen, prod_dimen, shipping_dimen)

CREATE VIEW tombined_table AS
SELECT  DISTINCT  market_fact.Ord_id, market_fact.Prod_id, market_fact.Ship_id, market_fact.Cust_id, market_fact.Sales, market_fact.Discount, market_fact.Order_Quantity, 
                         market_fact.Product_Base_Margin, shipping_dimen.Ship_Mode, shipping_dimen.Order_ID,shipping_dimen.Ship_Date, cust_dimen.Customer_Name, cust_dimen.Province, 
                         cust_dimen.Customer_Segment, cust_dimen.Region, prod_dimen.Product_Category, prod_dimen.Product_Sub_Category, orders_dimen.Order_Priority, orders_dimen.Order_Date
FROM         cust_dimen INNER JOIN
                         market_fact ON cust_dimen.Cust_id = market_fact.Cust_id INNER JOIN
                         shipping_dimen ON market_fact.Ship_id = shipping_dimen.Ship_id INNER JOIN
                         orders_dimen ON market_fact.Ord_id = orders_dimen.Ord_id INNER JOIN
                         prod_dimen ON market_fact.Prod_id = prod_dimen.Prod_id

SELECT * INTO combined_table FROM dbo.tombined_table


-- ////////////////////


-- 2. Maksimum sipariş sayısına sahip ilk 3 müşteriyi bulun.

select top 3 Cust_id,COUNT( Ord_id) count_of_orders 
from combined_table group by Cust_id order by COUNT( Ord_id) desc

-- /////////////////////////////



-- 3. Combine_table'da, Order_Date ve Ship_Date tarih farkını içeren DaysTakenForDelivery olarak yeni bir sütun oluşturun.
-- "DEĞİŞTİR TABLOSU", "GÜNCELLEME" vb. kullanın.

ALTER TABLE combined_table ADD DaysTakenForDelivery INT;

UPDATE combined_table
SET DaysTakenForDelivery = DATEDIFF(DAY,Order_Date,Ship_Date)

select DATEDIFF(DAY,Order_Date,Ship_Date) from combined_table

select * from combined_table

-- ////////////////////////////////


-- 4. Siparişinin teslim edilmesi için maksimum süreyi alan müşteriyi bulun.
-- "MAX" veya "TOP" kullanın
 
select TOP 1  Cust_id,Customer_Name,Order_Date,Ship_Date,DaysTakenForDelivery
from combined_table

order by DaysTakenForDelivery desc


-- ////////////////////////////



-- 5. Ocak ayındaki toplam benzersiz müşteri sayısını ve 2011'de tüm yıl boyunca her ay kaç tanesinin geri geldiğini sayın.
-- Tarih fonksiyonlarını ve alt sorguları kullanabilirsiniz.
create view cuslim as
select Cust_id from (
                      select  Cust_id,MONTH(Order_Date) ay,YEAR(Order_Date) yil
                      from combined_table
                      group by Cust_id,MONTH(Order_Date) ,YEAR(Order_Date)


                   ) Al
                      WHERE Al.yil=2011 AND  Al.ay=1

create view alti as
select *  from (
                 select 
                 MONTH(Order_Date) ay,YEAR(Order_Date) yil,Cust_id
			
                  from combined_table
                  GROUP BY MONTH(Order_Date),YEAR(Order_Date),Cust_id

              ) Alt
WHERE Alt.yil=2011 

select ay MONTH, COUNT(Cust_id) MONTHLY_NUM_OF_CUST from alti 
where Cust_id IN (SELECT Cust_id FROM cuslim)
group by ay





-- ////////////////////////////////////////


-- 6. İlk satın alma ile üçüncü satın alma arasında geçen süreye göre her kullanıcı için iade edilecek bir sorgu yazabilir,
-- Müşteri Kimliğine göre artan sırada
-- Pencere İşlevleriyle "MIN" kullanın

SELECT * FROM (

SELECT Cust_id,Order_Date, DENSE_RANK () OVER(partition by Cust_id order by Order_Date) dense_number,

ISNULL (CAST(LEAD (Order_Date, 2) OVER (PARTITION BY Cust_id ORDER BY Cust_id) AS VARCHAR(20)), 'last_order') FIRST_ORDER_DATE,
DATEDIFF(DAY,Order_Date,LEAD(Order_Date,2) OVER (partition by Cust_id order by Order_Date)) DAYS_ELAPSED
FROM combined_table
group BY Cust_id,Order_Date
) A 

WHERE dense_number=1 AND DAYS_ELAPSED > 0
ORDER BY A.Cust_id






-- /////////////////////////////////

-- 7. Hem 11. ürünü hem de 14. ürünü satın alan müşterileri döndüren bir sorgu yazın,
-- ayrıca bu ürünlerin tüm müşteriler tarafından satın alınan toplam ürün sayısına oranı.
-- CASE İfadesi, CTE, CAST ve/veya Toplama İşlevlerini kullanın

select * FROM (
select Cust_id,
               count(CASE
			   when Prod_id IN ('Prod_11') Then 1*Order_Quantity Else 0 END) P11,
			   count(CASE
			   WHEN Prod_id IN ('Prod_14')  THEN 1*Order_Quantity ELSE 0 END) P14, 
       COUNT(Prod_id) TOTAL_PROD,
	   CAST(1.0*SUM(CASE
			   when Prod_id IN ('Prod_11') Then 1 Else 0 END)/COUNT(Prod_id) AS decimal(3,2)) RATIO_P11,
       CAST(1.0*SUM(CASE
			   when Prod_id IN ('Prod_14') Then 1 Else 0 END)/COUNT(Prod_id) AS decimal(3,2)) RATIO_P14
from combined_table
group by Cust_id
) A
WHERE A.RATIO_P11 <> 0 AND A.RATIO_P14 <> 0

create view fun as
select  Count(Prod_id) cont from combined_table 

select Cust_id, Prod_id From combined_table WHERE Prod_id='Prod_11' 

select Cust_id,Prod_id from combined_table

WHERE Cust_id= 'Cust_138'
group by Cust_id,Prod_id



 

-- ////////////////



-- MÜŞTERİ SEGMENTASYONU



-- 1. Müşterilerin ziyaret günlüklerini aylık olarak tutan bir görünüm oluşturun. (Her log için üç alan tutulur: Cust_id, Year, Month)
-- Bu tür tarih işlevlerini kullanın. Daha sonra ihtiyaç duyabileceğiniz sütunları çağırmayı unutmayın.

select Cust_id, YEAR(Order_Date) YEAR,MONTH(Order_Date) MONTH
from combined_table
group by Cust_id,YEAR(Order_Date),MONTH(Order_Date)
order by Cust_id


-- //////////////////////////////



  -- 2.Kullanıcıların aylık ziyaretlerinin sayısını tutan bir "görünüm" oluşturun. (İş başlangıcından itibaren tüm ayları ayrı ayrı gösterin)
-- Daha sonra ihtiyaç duyabileceğiniz sütunları çağırmayı unutmayın.


select Cust_id, YEAR(Order_Date) YEAR,MONTH(Order_Date) MONTH,COUNT(DISTINCT Ord_id) NUM_OF_LOG
from combined_table
group by Cust_id,YEAR(Order_Date),MONTH(Order_Date)
order by Cust_id


-- //////////////////////////////


-- 3. Müşterilerin her ziyareti için, ziyaretin bir sonraki ayını ayrı bir sütun olarak oluşturun.
-- "DENSE_RANK" fonksiyonunu kullanarak ayları sıralayabilirsiniz.
-- daha sonra yukarıda yaptığınız sırayı kullanarak her ay için bir sonraki ayı gösteren yeni bir sütun oluşturun. ("KURŞUN" işlevini kullanın.)
-- Daha sonra ihtiyaç duyabileceğiniz sütunları çağırmayı unutmayın.

select * FROM
(

SELECT  DISTINCT Cust_id,YEAR(Order_Date) Yil,MONTH(Order_Date) Ay,
		DENSE_RANK() OVER (partition by YEAR(Order_Date) ORDER by MONTH(Order_Date)) denserank,
		ISNULL(CAST(DATEDIFF(month,Order_Date,LEAD(Order_Date, 1) OVER(PARTITION BY Cust_id ORDER BY Order_Date)) AS VARCHAR),'NULL') NEXT_VISIT_MONTH

FROM combined_table
) A
WHERE A.NEXT_VISIT_MONTH NOT IN ('0')





-- 4. Her müşterinin birbirini takip eden iki ziyareti arasındaki aylık zaman aralığını hesaplayın.
-- Daha sonra ihtiyaç duyabileceğiniz sütunları çağırmayı unutmayın.








select A.*, CASE 
	            WHEN A.Sip_Ad > 1 THEN 'REGULAR'  ELSE 'CHURN'
				END

	
	FROM (
	select Cust_id,Count( Ord_id) Sip_Ad, COUNT( DISTINCT FORMAT(Order_Date,'yyyy-MM')) Sip_Ay_Ad,
	from combined_table
	group by Cust_id) A
	













	select B.Cust_id,B.AVG_TIME_GAP,
                               CASE 
							   WHEN B.AVG_TIME_GAP IN ('NULL') THEN 'Churn' ELSE 'irregular' END CUST_LABELS
FROM
(
select * FROM
(

SELECT  DISTINCT Cust_id,YEAR(Order_Date) Yil,MONTH(Order_Date) Ay,
		DENSE_RANK() OVER (partition by YEAR(Order_Date) ORDER by MONTH(Order_Date)) denserank,
		ISNULL(CAST(DATEDIFF(month,Order_Date,LEAD(Order_Date, 1) OVER(PARTITION BY Cust_id ORDER BY Order_Date)) AS VARCHAR),'NULL') AVG_TIME_GAP

FROM combined_table
) A
WHERE A.AVG_TIME_GAP NOT IN ('0')
) B




-- ////////////////////////////////////


-- 5. Ortalama zaman boşluklarını kullanarak müşterileri kategorilere ayırın. Size en uygun etiketleme modelini seçin.
-- Örneğin:
-- Müşteri, ilk satın alımından bu yana aylar boyunca başka bir satın alma işlemi yapmadıysa, "kayıp" olarak etiketlenir.
-- Müşteri her ay bir satın alma işlemi yaptıysa "düzenli" olarak etiketlenir.
-- vb.
	select A.*, CASE 
	            WHEN A.Sip_Ad > 1 THEN 'REGULAR'  ELSE 'CHURN'
				END

	
	FROM (
	select Cust_id,Count( Ord_id) Sip_Ad, COUNT( DISTINCT FORMAT(Order_Date,'yyyy-MM')) Sip_Ay_Ad
	from combined_table
	group by Cust_id) A
	


	-- HER AY DUZENLI OLARAK ALISVERIS YAPAN MUSTERI YOK. TOPLAM 48 AYLIK DONEM ICIN KAC FARKLI AY ALISVERIS YAPTIKLARI LISTELENMISTIR:

	select * from combined_table


-- ////////////////////////////////




-- AYLIK SAKLAMA ORANI


-- İşin başlangıcından bu yana aylık müşteri elde tutma oranını bulun.
create view aylik as
select Cust_id,YEAR(Order_Date) yil,
       MONTH(Order_Date) ay,
       COUNT(Cust_id) sayi
from combined_table
GROUP BY  Cust_id,YEAR(Order_Date),
       MONTH(Order_Date)
ORDER BY 



SELECT YEAR(Order_Date) [YEAR],
       MONTH(Order_Date) [MONTH],
       CAST((COUNT(Cust_id)/6984.0) AS DECIMAL(3,2)) RETENTION_RATE
FROM combined_table
WHERE Cust_id IN(SElect Cust_id FROM aylik WHERE yil=2009 AND ay=1 )
GROUP BY  YEAR(Order_Date),
       MONTH(Order_Date)

ORDER BY [YEAR],[MONTH]





-- 1. Ay bazında elde tutulan müşteri sayısını bulun. (Zaman boşluklarını kullanabilirsiniz)
-- Zaman Boşluklarını Kullan

SELECT YEAR(Order_Date) [YEAR],
       MONTH(Order_Date) [MONTH],
       COUNT(distinct Cust_id) COUNT_CUSTOMER
FROM combined_table
WHERE Cust_id IN(SElect Cust_id FROM aylik WHERE yil=2009 AND ay=1 )
GROUP BY  YEAR(Order_Date),
       MONTH(Order_Date)

ORDER BY [YEAR],[MONTH]



-- ///////////////////


-- 2. Ay bazında elde tutma oranını hesaplayın.

-- Temel formül: o Ay Bazında Elde Tutma Oranı = 1.0 * İçinde Bulunulan Ayda Elde Tutulan Müşteri Sayısı / İçinde Bulunan Aydaki Toplam Müşteri Sayısı

-- İşlemleri tek bir geçici sorgu yerine parçalara bölmek daha kolaydır. Görünüm'ü kullanmanız önerilir.
-- İsterseniz CTE veya Alt Sorgu da kullanabilirsiniz.

-- Görünümleriniz veya tablolarınız arasında birleştirme türüne ve birleştirme sütunlarına dikkat etmelisiniz.

SELECT YEAR(Order_Date) [YEAR],
       MONTH(Order_Date) [MONTH],
       COUNT(DISTINCT Cust_id) COUNT_CUSTOMER,
	   CAST((COUNT(distinct Cust_id)*1.0/223) AS DECIMAL(4,3)) RETENTION_RATE
FROM combined_table
WHERE Cust_id IN(SElect Cust_id FROM aylik WHERE yil=2009 AND ay=1 )
GROUP BY  YEAR(Order_Date),
       MONTH(Order_Date)

ORDER BY [YEAR],[MONTH]


SELECT DISTINCT YEAR, MONTH, COUNT(Cust_id) OVER(PARTITION BY YEAR, MONTH ) ret_cust
FROM time_gaps
WHERE	visit_gap = 1
ORDER BY 1,2
SELECT DISTINCT YEAR, MONTH, COUNT(Cust_id) OVER(PARTITION BY YEAR, MONTH ) ret_cust
FROM time_gaps
ORDER BY 1,2





-- -//////////////////////////////
-- İyi şanslar!