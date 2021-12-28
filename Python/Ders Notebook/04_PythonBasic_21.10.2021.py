website = "https://www.clarusway.com"
course  = "Python Kursu ile kendi kendinize yatırım yapın - way to reinvent yourself"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?

result = len(course)


# 2- 'website' içinden www karakterlerini alın.
result = website[8:11]
#print(result)
# 3- 'website' içinden com karakterlerini alın.
# result = website[-3::]
# length = len(website)
# print(length)
# result = website[length-3:length]
# print(result)
# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
# result = course[:15]
# result = course[-15:]
# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
result = course[::-1]
print(result)





name, surname, age, job = 'Andrew','Fade', 37, 'mühendis' 

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Andrew Fade, Yaşım 37 ve mesleğim mühendis.' 
print('Benim adim '+ name + surname + ',' + ' Yasim ' + str(age) + ' ve meslegim ' + job + '.')

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = 'Hello world'
s = s[:6] +"W"+s[-4:]
print(s)
# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
print(*"abc", sep ="*")
# 
