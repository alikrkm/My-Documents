
---------------------------------ÖDEV2 (UPDATE – SELECT)---------------------------------------

--1-) Aşağıdaki tabloları oluşturarak verileri giriniz.

CREATE TABLE calisanlar
(
id CHAR(4),
isim VARCHAR2(50),
maas NUMBER(5),
CONSTRAINT id_pk PRIMARY KEY (id)
);
INSERT INTO calisanlar VALUES('1001', 'Ahmet Aslan', 7000);
INSERT INTO calisanlar VALUES( '1002', 'Mehmet Yılmaz' ,12000);
INSERT INTO calisanlar VALUES('1003', 'Meryem ', 7215);
INSERT INTO calisanlar VALUES('1004', 'Veli Han', 5000);


CREATE TABLE aileler
(
id CHAR(4),
cocuk_sayisi VARCHAR2(50),
ek_gelir NUMBER(5),
CONSTRAINT id_fk FOREIGN KEY (id) REFERENCES calisanlar(id)
);
INSERT INTO aileler VALUES('1001', 4, 2000);
INSERT INTO aileler VALUES('1002', 2, 1500);
INSERT INTO aileler VALUES('1003', 1, 2200);
INSERT INTO aileler VALUES('1004', 3, 2400);

--2-) Veli Han'ın maaşına %20 zam yapacak update komutunu yazınız.
--Güncellemeden sonra calisanlar tablosu aşağıda görüldüğü gibi olmalıdır.

UPDATE calisanlar
SET maas = maas*1.2
WHERE id = 1004

--3-) Maaşı ortalamanın altında olan çalışanların maaşına %20 zam yapınız.
--    Komut sonrası görünüm aşağıdaki gibidir.

UPDATE calisanlar
SET maas= maas*1.2
WHERE maas< (SELECT AVG(maas) FROM calisanlar)

--4-) Çalışanların isim ve cocuk_sayisi'ni listeleyen bir sorgu yazınız. Komut
--    sonrası görünüm aşağıdaki gibidir.

SELECT calisanlar.isim, aileler.cocuk_sayisi FROM calisanlar JOIN aileler ON calisanlar.id=aileler.id 

--5-) calisanlar' ın id, isim ve toplam_gelir'lerini gösteren bir sorgu yazınız.
--    toplam_gelir = calisanlar.maas + aileler.ek_gelir
--    Komut sonrası görünüm aşağıdaki gibidir.

SELECT calisanlar.id,calisanlar.isim, (calisanlar.maas+aileler.ek_gelir) as Toplam_Gelir FROM calisanlar JOIN aileler ON calisanlar.id=aileler.id 


--6-) Eğer bir ailenin kişi başı geliri 2000 TL den daha az ise o çalışanın
--    maaşına ek %10 aile yardım zammı yapınız.
--    kisi_basi_gelir = toplam_gelir / cocuk_sayisi + 2 (anne ve baba)

UPDATE calisanlar
SET maas= maas*1.1
WHERE  (SELECT (calisanlar.maas+aileler.ek_gelir)/(cocuk_sayisi+2) as ksbh 
from calisanlar JOIN aileler on calisanlar.id=aileler.id 
where ksbh < 2000)