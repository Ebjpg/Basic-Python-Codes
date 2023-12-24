sayi = int(input("Bir Sayi Giriniz: "))

if 0 < sayi < 100:
    print(f"{sayi} 0-100 Arasındadır")
else:
    print(f"{sayi} 0-100 Arasında Değildir.")

if sayi % 2 == 0 and sayi > 0:
    print(f"{sayi} pozitif çift sayıdır.")
