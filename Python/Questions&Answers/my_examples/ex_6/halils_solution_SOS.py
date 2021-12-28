a = ["E", "E", "E"]
b = ["E", "E", "E"]
c = ["E", "E", "E"]
d = ["XXX", "OOO"]


def yataykont(a):
    b = "".join(a)
    if any(i in b for i in d):
        if d[0] in b:
            print("X kazandi ")
        elif d[1] in b:
            print("O kazandi ")


def dikeykont(a, b, c):
    ver = list(map(lambda x, y, z: x + y + z, a, b, c))
    if any(i in ver for i in d):
        if d[0] in ver:
            print("X kazandi ")
        elif d[1] in ver:
            print("O kazandi")


def capraz(a, b, c):
    if a[0] == b[1] == c[2] or a[2] == b[1] == c[0]:
        if (a[0] == "X" and b[1] != "E") or (a[2] == "X" and b[1] != "E"):
            print("X kazandiC")
        elif (a[0] == "O" and b[1] != "E") or (a[2] == "O" and b[1] != "E"):
            print("O kazandi")


def kontrol(a, b, c):
    dikeykont(a, b, c)
    yataykont(a)
    yataykont(b)
    yataykont(c)
    capraz(a, b, c)
    if bool(dikeykont(a, b, c)) or bool(yataykont(a)) or bool(yataykont(b)) or bool(yataykont(c)) or bool(capraz(a, b, c)):
        return True


countx = 0
conto = 1
i = 0
while i < 10 and kontrol(a, b, c) != True:
    i += 1

    kontrol(a, b, c)
    if conto > countx:
        countx += 1

        x = input("x bitte ihre komb. eingegeben Z.B: 12 ").upper()

        if int(x[0]) == 1:
            if a[int(x[1])-1] == "E":
                a[int(x[1])-1] = "X"
                print(a, b, c, sep="\n")

            else:
                x = input(
                    "x bitte ihre komb. nochmal eingegeben weil ihre column ist schon da Z.B: 12 ").upper()
        elif int(x[0]) == 2:
            if b[int(x[1])-1] == "E":
                b[int(x[1])-1] = "X"
                print(a, b, c, sep="\n")

            else:
                x = input(
                    "x bitte ihre komb. nochmal eingegeben weil ihre column ist schon da Z.B: 12 ").upper()

        elif int(x[0]) == 3:
            if c[int(x[1])-1] == "E":
                c[int(x[1])-1] = "X"
                print(a, b, c, sep="\n")

            else:
                x = input(
                    "x bitte ihre komb. nochmal eingegeben weil ihre column ist schon da Z.B: 12 ").upper()

    else:
        conto += 1
        o = input("o bitte ihre komb. eingegebenZ.B: 11").upper()
        if int(o[0]) == 1:
            if a[int(o[1])-1] == "E":
                a[int(o[1])-1] = "O"
                print(a, b, c, sep="\n")
            else:
                o = input(
                    "O bitte ihre komb. nochmal eingegeben weil ihre column ist schon da Z.B: 12 ").upper()
        elif int(o[0]) == 2:
            if b[int(o[1])-1] == "E":
                b[int(o[1])-1] = "O"
                print(a, b, c, sep="\n")
            else:
                o = input(
                    "O bitte ihre komb. nochmal eingegeben weil ihre column ist schon da Z.B: 12 ").upper()

        elif int(o[0]) == 3:
            if c[int(o[1])-1] == "E":
                c[int(o[1])-1] = "O"
                print(a, b, c, sep="\n")
            else:
                o = input(
                    "O bitte ihre komb. nochmal eingegeben weil ihre column ist schon da Z.B: 12 ").upper()
