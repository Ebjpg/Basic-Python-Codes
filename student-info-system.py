ogrenciler = {}

for i in range(0, 3):
    ogrNo = input("Öğrenci No: ")
    ogrAdi = input("Öğrenci Adı: ")
    ogrSoyadi = input("Öğrenci Soyadı: ")
    ogrTel = input("Telefon: ")
    ogrenciler.update({
        ogrNo: {
            "isim": ogrAdi,
            "soyisim": ogrSoyadi,
            "telefon": ogrTel,
        }
    })

print(ogrenciler)
