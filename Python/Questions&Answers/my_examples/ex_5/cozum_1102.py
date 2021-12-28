x = int(input("Bir sayı giriniz: "))
t = int(input("tabani giriniz: "))
a = x
s = []
while a >= t:
    k = a % t
    s.append(k)
    a = a//t
l = [a]
s.reverse()
l.extend(s)
print(f"{x} sayisinin {t} tabaninda ki esiti : ", *l, sep="")
