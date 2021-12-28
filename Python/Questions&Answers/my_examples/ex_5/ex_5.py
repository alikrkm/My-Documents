sayı = int(input("Sayı giriniz : "))
taban = int(input("Kaç tabanında görmek istersiniz : "))

sonuc = ""
counter = 1

while True:
    if sayı - (taban ** counter) < 0:
        break
    counter += 1

print("Girdiğiniz sayı =", sayı)

for i in range(counter-1, -1, -1):
    if sayı - (taban ** i) >= 0:
        for j in range(taban, 0, -1):
            if sayı - j * (taban ** i) >= 0:
                sayı -= j * (taban ** i)
                if j > 9:
                    sonuc += chr(ord("A") + j - 10)
                else:
                    sonuc += str(j)
    else:
        sonuc += "0"

print("Sonucunuz {} tabanında ve {} basamaklıdır. Sonuç = {}.".format(taban, counter, sonuc))