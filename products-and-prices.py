urunler = []
urunSayisi = int(input("Kaç Adet Ürün Eklenecek: "))
i = 0

while i < urunSayisi:
    urunAdi = input("Ürün Adı Giriniz: ")
    urunFiyati = input("Ürün Fiyatı Giriniz: ")
    urunler.append({
        "Ürün Adı": urunAdi,
        "Ürün Fiyatı": urunFiyati,
    })
    i += 1

print(urunler)
