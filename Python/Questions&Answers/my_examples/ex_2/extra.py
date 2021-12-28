x = int(input("sayi gir"))

for i in range(1, x + 1):

    print("{}{}".format(i, ((i % 10 == 1 and "st")
                            or (i % 10 == 2 and "nd")
                            or (i % 10 == 3 and "rd")
                            or "th")))
