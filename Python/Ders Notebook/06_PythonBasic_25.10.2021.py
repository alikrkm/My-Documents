website = "https://www.clarusway.com"
course  = "Python Kursu ile kendi kendinize yatırım yapın - Way to Reinvent Yourself"


# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result = " Hello World ".strip()
# 2- 'www.edabit.com' içindeki edabit bilgisi haricindeki her karakteri silin.
result = "www.edwwwabit.com".lstrip("w.").rstrip(".com")
# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result = course.lower()
# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
result = website.count("w")
result = website.count("www")
result = website.count('www',0,10)
# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
result = website.startswith("www")
result = website.endswith('com')
# 6-  'website' içinde '.com' ifadesi var mı?
result = website.find("com")
result = website.rfind("com")
result = website.index("com")
result = website.rindex("com")
# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result = course.isalpha()
result = 'Hello'.isalpha()
result = course.isdigit()
result = '123'.isdigit()
# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result = "contents".center(50, "*")
result = "contents".ljust(50, "*")
result = "contents".rjust(50, "*")
# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result = course.replace(" ", "-", 5)
# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
result = 'Hello World'.replace('World','There')
# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.
result = course.split(" ")

print(result)   

# 12- Write a program to check if a given string is a Palindrome.
# A palindrome reads same from front and back e.g.- aba, ccaacc, mom, etc.
# INPUT:  aba
# OUTPUT: True
a = "adanada"
print(type((a == a[::-1])))
print(a == a[::-1])

print(5^20)