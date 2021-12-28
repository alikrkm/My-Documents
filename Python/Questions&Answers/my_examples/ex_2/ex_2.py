x = int(input("sayi gir : "))

# print("After {} day{}.".format(x,"logical operations"))

print("After {} day{}.".format(x, (x-1 and "s") or ""))

# print("{}{}".format(x, "logical operations" )) # 1 st 2 nd 3 rd 4546 th

# 1st
# 2nd
# 3rd
# 4.... th

print("{}{}".format(x, (x == 3 and "rd") or (
    x == 2 and "nd") or (x == 1 and "st") or "th"))

print("{}{}".format(x, (not (x-3) and "rd" or not (x-2)
                        and "nd" or (not (x-1) and "st" or "th"))))

print('{}{}'.format(x, (x == 1 and "st") or (x == 2 and "nd")
                    or (x == 3 and "rd") or (x >= 4 and "th")))
