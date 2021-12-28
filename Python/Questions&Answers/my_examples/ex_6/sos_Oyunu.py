Sıra_1 = input("Oyuna ilk kim başlasın ? (S veya O) : ").upper()
Sıra_2 = "S" if Sıra_1 == "O" else "O"

sayaç = 0
sonuç = 'Berabere'

oyun_tahtası = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]


def check_size(row, col):
    while row < 1 or row > 3 or col < 1 or col > 3:
        print()
        print("Girdiğiniz satır sütun bilgileri tahta boyutlarından faklıdır. Lütfen tekrar 1-2-3 olan bir satır ve sütun u işaretleyiniz...")
        print()
        row = int(
            input("Kaçıncı satırı işaretlemek istediğinizi seçiniz :   "))
        col = int(
            input("Kaçıncı sütunu işaretlemek istediğinizi seçiniz :   "))
    return [row, col]


def check_empty(row, col):
    while oyun_tahtası[row - 1][col - 1] != " ":
        print()
        print("Girdiğiniz satır sütun içeriği doludur. Lütfen tekrar boş olan bir satır ve sütun u işaretleyiniz...")
        print()
        row = int(
            input("Kaçıncı satırı işaretlemek istediğinizi seçiniz :   "))
        col = int(
            input("Kaçıncı sütunu işaretlemek istediğinizi seçiniz :   "))
        while row < 1 or row > 3 or col < 1 or col > 3:
            print()
            print("Girdiğiniz satır sütun bilgileri tahta boyutlarından faklıdır. Lütfen tekrar 1-2-3 olan bir satır ve sütun u işaretleyiniz...")
            print()
            row = int(
                input("Kaçıncı satırı işaretlemek istediğinizi seçiniz :   "))
            col = int(
                input("Kaçıncı sütunu işaretlemek istediğinizi seçiniz :   "))
    return [row, col]


while sayaç < 9 and sonuç == "Berabere":

    print()
    print(*oyun_tahtası, sep="\n\n")
    print()

    print("{} oyuncusunun sırası".format(
        Sıra_1 if sayaç % 2 == 0 else Sıra_2))
    print("--------------------")

    satır = int(input("Kaçıncı satırı işaretlemek istediğinizi seçiniz :   "))
    sütun = int(input("Kaçıncı sütunu işaretlemek istediğinizi seçiniz :   "))

    satır, sütun = check_size(satır, sütun)

    satır, sütun = check_empty(satır, sütun)

    oyun_tahtası[satır - 1][sütun - 1] = Sıra_1 if sayaç % 2 == 0 else Sıra_2

    vertical = list(map(lambda *x: [*x], *oyun_tahtası))

    for i in range(len(oyun_tahtası)):
        if len(set(oyun_tahtası[i])) == 1 and oyun_tahtası[i][0] != ' ':
            sonuç = oyun_tahtası[i][0]
            break
        elif len(set(vertical[i])) == 1 and vertical[i][0] != ' ':
            sonuç = vertical[i][0]
            break

    if sonuç == 'Berabere':
        if oyun_tahtası[0][0] == oyun_tahtası[1][1] == oyun_tahtası[2][2] and oyun_tahtası[0][0] != ' ':
            sonuç = oyun_tahtası[0][0]
        elif oyun_tahtası[0][2] == oyun_tahtası[1][1] == oyun_tahtası[2][0] and oyun_tahtası[0][2] != ' ':
            sonuç = oyun_tahtası[0][2]

    sayaç += 1
    print()
    print(sayaç, ". elin sonu :")

print()
print(*oyun_tahtası, sep="\n")
print()
print(sonuç if (sonuç == "Berabere") else "Kazanan oyuncu " + sonuç)
