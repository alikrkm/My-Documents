""" TASK 1;
A number is said to be Harshad if it's exactly divisible by the sum of its digits. Create a function that determines whether a number is a Harshad or not.

is_harshad(75) ➞ False
# 7 + 5 = 12
# 75 is not exactly divisible by 12

is_harshad(171) ➞ True
# 1 + 7 + 1 = 9
# 9 exactly divides 171

is_harshad(481) ➞ True

is_harshad(89) ➞ False

is_harshad(516) ➞ True

is_harshad(200) ➞ True

****************************************************************************"""
# # TASK 1
# num = input("Bir sayı giriniz: ")
# def summary(num):
#     sum = 0
#     for i in num:
#         sum += int(i)
#     return int(num) % sum == 0
# print(summary(num))

"""****************************************************************************
TASK 2;
Create a function that takes an integer n and returns the factorial of factorials. 

See below examples for a better understanding:

fact_of_fact(4) ➞ 288
# 4! * 3! * 2! * 1! = 288

fact_of_fact(5) ➞ 34560

fact_of_fact(6) ➞ 24883200


***************************************************************"""
# # TASK 2
# num = int(input("Bir sayı giriniz: "))
# faktöriyel_2 = 1
# if num >= 0:
#     for i in range(1,num+1):
#         faktöriyel_1 = 1
#         for j in range(1, i+1):
#             faktöriyel_1 *= j
#     faktöriyel_2 *= faktöriyel_1
# else:
#         print("pozitif sayı girdiginizden emin olunuz!!!")
# print(faktöriyel_2)


"""****************************************************************

TASK 3;
Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }

***********************************************************************"""
# # TASK 3:

# # pluralize = ["cow", "pig", "cow", "cow"] # { "cows", "pig" }
# # pluralize = ["table", "table", "table"] # { "tables" }
# pluralize = ["chair", "pencil", "arm"] # { "chair", "pencil", "arm" }

# new_pluralize = []

# for i in pluralize:
#     if pluralize.count(i) > 1:
#         plural = i.replace(i, i + "s")
#         new_pluralize.append(plural)
#     else:
#         new_pluralize.append(i)

# print(set(new_pluralize))

"""****************************************************************
TASK 4;
Create a function that takes a number num and returns each place value in the number.

num_split(39) ➞ [30, 9]

num_split(-434) ➞ [-400, -30, -4]

num_split(100) ➞ [100, 0, 0]


******************************************************************"""
# # TASK 4:

num = input("sayı giriniz: ")
liste_num = list(num)
liste_num.reverse()

def eksi(x):
    return 0-x

if int(num) >= 0:
    for i in range(len(liste_num)):
        liste_num[i] = list(map(int,liste_num))[i] * (10**i)
        liste_num.reverse()
    print(liste_num)
else:
    liste_num.pop()
    for i in range(len(liste_num)):
        liste_num[i] = list(map(int,liste_num))[i] * (-10**i)*(-1)
        liste_num.reverse()
    print(list(map(eksi,liste_num)))

"""**********************************************************************
TASK 5; 
Verilen bir kuruluşu oluşturan kelimelerin baş harflerini kullanarak kısaltma oluşturan bir fonksiyon yazınız.

*********************************************************************"""
# TASK 5:

# name = input("Kuruslusun adını giriniz: ")
# name = name.title()
# for harf in name:
#     if ord("A") <= ord(harf) <= ord("Z"):
#         print(harf, end=".")

"""***********************************************************************

TASK 6;
Question 1
It takes 21 seconds to wash your hands and help prevent the spread of COVID-19.
Create a function that takes the number of times a person washes their hands per day N and the number of months they follow this routine nM and calculates the duration in minutes and seconds that person spends washing their hands.
Examples
(8, 7) ➞ "588 minutes and 0 seconds"
(0, 0) ➞ "0 minutes and 0 seconds"
(7, 9) ➞ "661 minutes and 30 seconds"
Notes
Consider a month has 30 days.
Wash your hands.

************************************************************************"""
# TASK 6:

# SORUYU ANLAMADIM!!!! GEC COKTA SACMASORUYA BENZİYOR...

"""************************************************************************************************

TASK 7;
Question 2
Write a function that finds the largest even number in a list. Return -1 if not found. The use of built-in functions max() and sorted() are prohibited.
Examples
[3, 7, 2, 1, 7, 9, 10, 13] ➞ 10
[1, 3, 5, 7] ➞ -1
[0, 19, 18973623] ➞ 0
Notes
Consider using the modulo operator %

***************************************************************************"""
# TASK 7:

# liste = [3, 7, 2, 1, 7, 9, 10, 13] # 10
# liste = [1, 3, 5, 7] # -1
# liste = [0, 19, 18973623] # 0
# new_liste = []
# for i in liste:
#     if not (i % 2):
#         new_liste.append(i)
# if not new_liste:
#     print("-1")
# else:
#     print(max(new_liste))

"""*******************************************************************************

TASK 8;
Question 3
Create a function that determines whether a number is Oddish or Evenish. A number is Oddish if the sum of all of its digits is odd, and a number is Evenish if the sum of all of its digits is even. If a number is Oddish, return "Oddish". Otherwise, return "Evenish".
For example, (121) should return "Evenish", since 1 + 2 + 1 = 4. (41) should return "Oddish", since 4 + 1 = 5.
Examples
(43) ➞ "Oddish"
4 + 3 = 7
7 % 2 = 1
(373) ➞ "Oddish"
3 + 7 + 3 = 13
13 % 2 = 1
(4433) ➞ "Evenish"
4 + 4 + 3 + 3 = 14
14 % 2 = 0

*****************************************************************"""
# TASK 8:
# number = input("Enter a number: ")
# def OddishORevenish(number):
#     summary = sum(list(map(int,number)))
#     if not (summary % 2):
#         return "Evenish"
#     else:
#         return "Oddish"
# print(OddishORevenish(number))


"""************************************************************************************

TASK 9;
Program to print pyramid a using numbers.(User enter the numbers of rows)

zb. 
1
2 2
3 3 3
4 4 4 4

********************************************************************"""

# TASK 9:

# num = int(input("Enter a number, I have a surpriz for you...  "))
# for i in range(num+1):
#     print(* i * str(i))

"""*********************************************************************************

TASK 10;
Question 5
Fruit salads are served best when the fruits are sliced and diced into small chunks!
For this challenge, slice each fruit in half and sort the chunks alphabetically. This recipe tastes best when the chunks are joined together to make a string.
Worked Example
["apple", "pear", "grapes"] ➞ "apargrapepesple"
Chunks: ["ap", "ple", "pe", "ar", "gra", "pes"]
Sorted chunks: ["ap", "ar", "gra", "pe", "pes", "ple"]
Final string: "apargrapepesple"
Examples
["apple", "pear", "grapes"] ➞ "apargrapepesple"
["raspberries", "mango"] ➞ "erriesmangoraspb"
["banana"] ➞ "anaban"
Notes
If a fruit has an odd number of letters, make the right side larger than the left.
For example: "apple" will be sliced into "ap" and "ple".
All fruits will be given in lowercase.

***********************************************************************"""
# TASK 10:

# fruits = ["apple", "pear", "grapes"] # "apargrapepesple"
# fruits = ["raspberries", "mango"] # "erriesmangoraspb"
# fruits = ["banana"] # "anaban"
# Chunks = []
# for fruit in fruits:
#     if (len(fruit) == 2) or (len(fruit) == 3):
#         Chunks.append(fruit)
#     else:
#         Chunks.extend([fruit[:len(fruit)//2],fruit[len(fruit)//2:]]) # alttaki gibi append de kullanılabilirdi!
#         # Chunks.append(fruit[:int((len(fruit)-1)/2)])
#         # Chunks.append(fruit[int((len(fruit)-1)/2):])
# print(''.join(sorted(Chunks)))


"""*****************************************************************************

TASK 11;
Question 6
Given a positive integer N, The task is to write a Python program to check if the number is prime or not.
Definition:
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
The first few prime numbers are {2, 3, 5, 7, 11, ….}.

*************************************************************************"""
# TASK 11:

# number = int(input("Enter a number! I will check it whether this number is a prime number or not... "))
# x = True
# for i in range(2,number):
#     if number % i == 0 :
#         x = False
#         print("This number is not a prime number")
#         break
# if x:
#     print("This number is a prime number")

"""***********************************************************************************

TASK 12;
Question 7
Create a function that takes a word and extends all vowels by a number num.
Examples
"Hello", 5 ➞ "Heeeeeelloooooo"
"Edabit", 3 ➞ "EEEEdaaaabiiiit"
"Extend", 0 ➞ "Extend"
****************************************************************"""
# TASK 12:
# num = int(input("Enter a number: "))
# word = input("Enter a word: ")
# Sadece ingilizce alfabedeki vowels lar dikkate alındı!
# vowel = set("aeiouAEIOU")
# new_word = ""
# for i in word:
#     if i in vowel:
#         i = i*(num+1)
#         new_word += i
#     else:
#         new_word += i
# print(new_word)
