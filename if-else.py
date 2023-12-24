vize = int(input("Vize Notunu Giriniz: "))
vize2 = int(input("Vize 2 Notunu Giriniz: "))
final = int(input("Final Notunu Giriniz: "))
ortalama = (vize + vize2) / 2 * 0.6 + final * 0.4

if ortalama >= 50:
    print("Ortalama {} dersten geçtiniz.".format(ortalama))
else:
    print("Ortalama {} dersten kaldınız.".format(ortalama))
