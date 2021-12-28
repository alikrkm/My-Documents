aile_no = int(input("1. , 2. veya 3. aileden hangisini istersiniz ? : "))
ebeveyn_sayisi = 2
cocuk_sayisi = aile_no + 1
tuketim = (ebeveyn_sayisi * 9) + (cocuk_sayisi * 4)
stok = 60
alinan = [21 * 6, 11 * 6, 19 * 6]

for gun in range(1, 20):
    market = [int((gun - 1) / 7) + 1, int((gun - 1) / 3) +
              1, int((gun - 1) / 5) + 1]
    kalan = stok + alinan[aile_no-1] * market[aile_no-1] - tuketim * gun
    # print(gun, ". günün sonunda kalan ekmek = ", kalan)
    if kalan <= 0:
        print("1. sorunun cevabı :",
              market[aile_no-1], ". alışverişe gitmelerinden sonra ekmek stokları tükenir.")
        print("2. sorunun cevabı :", gun,
              ". günün sonunda ekmek stokları tükenir.")
        break

son_gun = gun
iteration = 0
new_gun = 0

while (new_gun) < (son_gun + 5):
    iteration += 1
    for new_gun in range(1, 20):
        market2 = [int((new_gun - 1) / 7) + 1,
                   int((new_gun - 1) / 3) + 1, int((new_gun - 1) / 5) + 1]

        kalan = stok + (alinan[aile_no-1] + (6 * iteration)) * \
            market2[aile_no-1] - tuketim * new_gun
        if kalan <= 0:
            break

print("3. sorunun cevabı : Her alışverişe gidildiğinde", iteration, "adet fazla paket almak gerekli")