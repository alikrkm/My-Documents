test = input("bir dizi yazılar ... : ")

words  = test.split()

for i in range(len(words)):
    if words[i].isdigit():
        print(words[i])
    else:
        ascii = []
        for j in range(len(words[i])):
            ascii.append(ord(words[i][j]))
        print(*ascii, sep=", ")
        
        
text = test
liste1 = list(text)
for x in range(0, len(liste1)):
    if ord(liste1[x])!=32:            # BOSLUK KONTROLU
        if 47<ord(liste1[x]) <58:   # 0-9 ARASI ASCII KODU
            print(liste1[x], end="")      # EGER SAYI ISE YAZDIR AMA ALT SATIRA GECME

    elif ord(liste1[x]) == 32 and ord(liste1[x+1])==32:

        print("", end="")                          # 2 kere BOSLUK OLDUGUNDA ALT SATIRA GECMEmeK ICIN
    elif ord(liste1[x]) == 32:
        print("\n")             # 2 kere BOSLUK OLDUGUNDA ALT SATIRA GECMEmeK ICIN