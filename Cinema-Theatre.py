secim = input("Sinema için (1), Tiyatro için (2) tuşlayınız: ")
ogrenci = input("Öğrenci misiniz(E/H): ")
ucret = 0

if secim == '1':
    ucret = 15  # Sinema
elif secim == '2':
    ucret = 10  # Tiyatro

if ogrenci.lower() == 'e':
    ucret /= 2  # %50 indirim

print("Ödemeniz gereken ücret: {}".format(ucret))
