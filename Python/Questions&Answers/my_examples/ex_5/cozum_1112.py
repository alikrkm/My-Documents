zahl = int(input("bitte ihre Zahl eingegeben"))
basevalue = int(input("bitte ihre base value eingegeben"))
list1 = []
kalan = zahl
while kalan > basevalue:
    list1.append(str(kalan % basevalue))
    if kalan // basevalue > basevalue:
        kalan = kalan // basevalue
    else:
        list1.append(str(kalan//basevalue))
        break
list1.reverse()
alt = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
if basevalue < 16:
    print("{} = ({}){} ".format(zahl, "".join(
        list1), str(basevalue).translate(alt)))
else:
    hexa = list(hex(zahl))
    print("".join(hexa[2:]))
