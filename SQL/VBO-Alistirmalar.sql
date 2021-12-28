------------------------VBO - ALISTIRMALAR-----------------------
-- 1-)
-- SELECT count(*) FROM Orders;

--2-)
--SELECT count(DISTINCT CustomerID) from 

--3-)
--SELECT Country, count(CustomerID) FROM Customers GROUP BY Country

--4-)
--SELECT * FROM Customers WHERE Country IN('Brazil','USA')

--5-)
--SELECT Country,City,count(CustomerID) FROM Customers GROUP BY Country,City

--6-)
--SELECT Address FROM Customers WHERE Address LIKE '%da%'

--7-)
--SELECT CustomerName FROM Customers WHERE Country='Germany' AND City='Berlin'

--8-)
--SELECT CustomerName FROM Customers WHERE Country='Canada' AND CustomerName LIKE '%in%'

--9-)
--SELECT ProductName,Price FROM Products WHERE Price BETWEEN 40 AND 90

--10-)
--SELECT ProductName as Urunun_Ismi,Price as Urunun_Fiyati, (Price*Price) as Urunun_fiyatinin_karesi FROM Products WHERE Price > 30

--11-)
--SELECT DISTINCT CategoryName FROM Products JOIN Categories ON Products.CategoryID=Categories.CategoryID

--12-)
--SELECT AVG(Price) FROM Products JOIN Categories ON Products.CategoryID=Categories.CategoryID AND Categories.CategoryID=1

--13-)
--SELECT sum(Price) FROM Products JOIN Customers ON Products.ProductID=Customers.CustomerID JOIN Orders ON Customers.CustomerID=Orders.CustomerID WHERE Country= 'USA':

--14-)
--SELECT CategoryName,round(avg(Price))FROM Categories JOIN Products ON Categories.CategoryID=Products.CategoryID GROUP BY CategoryName;

--15-)
--SELECT FirstName,LastName, sum(Price) FROM Employees JOIN Orders ON Employees.EmployeeID=orders.EmployeeID JOIN OrderDetails ON Orders.OrderID=OrderDetails.OrderID JOIN Products ON OrderDetails.ProductID=Products.ProductID GROUP BY FirstName ORDER BY sum(Price) DESC;

--16-)
--SELECT CategoryName, round(avg(Price)) FROM  Customers JOIN Orders ON Customers.CustomerID=Orders.CustomerID JOIN OrderDetails ON Orders.OrderID=OrderDetails.OrderID  JOIN Products ON OrderDetails.ProductID=Products.ProductID JOIN Categories ON Categories.CategoryID=Products.CategoryID WHERE Customers.Country ='Germany' GROUP BY CategoryName;

--17-)
-- SELECT Categories.CategoryName, round(AVG(Products.Price)) FROM Categories
-- JOIN Products ON Categories.CategoryID=Products.CategoryID
-- JOIN  Suppliers ON Suppliers.SupplierID=Products.ProductID
-- JOIN OrderDetails ON Products.ProductID=OrderDetails.ProductID 
-- JOIN Orders ON OrderDetails.OrderID=Orders.OrderID 
-- WHERE Suppliers.Country IN ('Germany','USA')
-- GROUP BY Categories.CategoryName;


--18-)
-- SELECT round(avg(Price)) FROM Products 
-- JOIN OrderDetails ON Products.ProductID=OrderDetails.ProductID 
-- JOIN Orders ON OrderDetails.OrderID=Orders.OrderID 
-- WHERE OrderDate  LIKE '%.06.199%' OR OrderDate LIKE '%.07.199%' OR OrderDate LIKE '%.08.199%'  

--19-) 
-- SELECT CustomerName, max(Price) as maks FROM Products 
-- JOIN OrderDetails ON Products.ProductID=OrderDetails.ProductID 
-- JOIN Orders ON OrderDetails.OrderID=Orders.OrderID 
-- JOIN Customers ON Orders.CustomerID=Customers.CustomerID
-- WHERE OrderDate  LIKE '%.1997%'
-- GROUP BY CustomerName
-- ORDER BY maks DESC

--20-)
-- SELECT Employees.FirstName,Employees.LastName,Employees.EmployeeID, count(Orders.OrderID) as Sip_Say FROM Products 
-- JOIN OrderDetails ON Products.ProductID=OrderDetails.ProductID 
-- JOIN Orders ON OrderDetails.OrderID=Orders.OrderID 
-- JOIN Employees ON Orders.EmployeeID=Employees.EmployeeID 
-- WHERE Orders.OrderDate LIKE '%.1997%'
-- GROUP BY Employees.EmployeeID
-- ORDER BY Sip_Say DESC;







