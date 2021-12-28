sayi = int(input('bir sayi giriniz : '))
basamak = int(input('cevirmek istediginiz tabani giriniz : '))
kalan = []
bölüm = sayi/basamak
while bölüm >= basamak:
    bölüm = sayi//basamak
    kalan.append(sayi % basamak)
    sayi = bölüm
kalan.reverse()
kalan.insert(0, bölüm)
kalan
son = ''
for i in kalan:
    son += str(i)
print(int(son))
