"""
sayi1=input("1. Sayiyi Giriniz :")
sayi2=input("2. Sayiyi Giriniz :")
toplam=int(sayi1)+int(sayi2)
print("Toplam= ",toplam)


sayi1=input("Bir sayi giriniz :")
sayi2=input("Bir sayi daha giriniz :")
ortalama=(int(sayi1)+int(sayi2))/2
print("Girdiğiniz iki sayının ortalaması = ",ortalama)



vize=input("Vize Notu :")
final=input("Final Notu :")
ortalama=int(vize)*0.4+int(final)*0.6
print("Ortalamanız: ",ortalama)


"""

#girilen sayı tek mi çift mi ?
"""
sayi=input("Bir Sayi Giriniz : ")
if(int(sayi)%2==0):
    print("Girdiginiz Sayi Çifttir !")
else:
    print("Girdiginiz Sayi Tektir !")
"""

#girilen sayı negatif mi pozitif mi sıfır mı ?
"""
sayi=input("Bir Sayi Giriniz :")
if(int(sayi)>0):
    print("Girilen Sayi Pozitiftir !")
elif(int(sayi)<0):
    print("Girilen Sayi Negatiftir !")
else:
    print("Girilen Sayi Sıfırdır !")
"""

#1-100 arası tel sayıları ekranda listeleyen program
"""for i in range(1,100,2):
    print(i)
"""

#1-100 Arası 3′ e ve 5′ e tam bölünen sayıları bulan kod
"""
for i in range(1,101):
    if(int(i)%3==0 and int(i)%5==0):
        print(i)
"""
#1 den Kullanıcının Girdiği Sayıya Kadar Sayıları Listeleyen
"""
sayi=input("Bir Sayi Giriniz :")
for i in range(1,int(sayi)):
    print(i)
"""
#Kenarları Girilen Dikdörtgenin Alanı ve Çevresini Bulan

"""
kisaKenar=input("Kısa Kenar Uzunlugu: ")
uzunKenar=input("Uzun Kenar Uzunlugu: ")
alan=int(kisaKenar)*int(uzunKenar)
cevre=(int(kisaKenar)+int(uzunKenar))*2
print("Dikdörtgenin Alanı {} ,Dikdörtgenin Çevresi {} ".format(alan,cevre))
"""

#Girilen metnin harflerini alt alta yazdıran
"""
metin=input("")
sayac=0
while(sayac<len(metin)):
    print(metin[sayac])
    sayac+=1

"""

#Kullanıcın girdiği iki sayı arasındaki sayıların toplamını gösteren
"""
sayi1=input("Bir Sayi Giriniz:")
sayi2=input("Bir Sayi daha Giriniz :")
toplam=0
for i in range(int(sayi1),int(sayi2)):
    toplam+=i
print(toplam)
"""

#Kullanıcıya sinema ya da tiyatro tercihi sorulsun+. Sinema izlemek için 15 TL, tiyatro için 10 TL ödenmesi gerekmedir.
#Öğrencilere %50 indirim yapıldığı düşünülerek öğrenci ise indirim yapılan; öğrenci değilse indirimsiz tutarı hesaplayarak ekrana yazdıran kodu yazınız
"""
secim = input("Sinema için (1), Tiyatro için (2) tuşlayınız : ")
ogrenci = input("Öğrenci misiniz(E/H) : ")
ucret = 0

# indirimsiz ücret hesaplama
if secim == '1':
    ucret = 15  # sinema
elif secim == '2':
    ucret = 10  # tiyatro

# öğrenci indirimi
if ogrenci == 'E' or ogrenci == 'e':
    ucret = ucret / 2  # %50

print("Ödemeniz gereken ücret :{}".format(ucret))
"""

#Fonksiyon kullanarak yarıçapı girilen dairenin alanını hesaplayan
"""
def daireAlan(yaricap):
    alan=int(yaricap)*int(yaricap)*3.14
    print("Dairenin Alanı= ",float(alan))

r=input("Yaricap degerini giriniz :")
daireAlan(r)
"""





#Fonksiyon kullanarak genişliği ve yüksekliği girilen dikdörtgenin alanını hesaplayan
"""
def dikdortgenAlan(yukseklik,genislik):
    alan=int(yukseklik)*int(genislik)
    print("Dikdörtgenin Alanı = ",float(alan))


h=input("Dikdörtgenin Yüksekliğini Giriniz :")
k=input("Dikdörtgenin Genisligini Giriniz :")
dikdortgenAlan(h,k)
"""

#üs alma = int(number)**int(number)
#strip() = bir karakterden baştan bir karakter sondan siler.
#lstrip() = soldan karakter siler.parametre olarak "" içinde string alır . rstrip() olursa sağdan siler
"""
website = "http://www.sadikturan.com/"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"
emir ="eMiRhaNdaGdelen.com"
alfabe="abcdefg"
print(len(course))
print(website[7:10])
print(website.lstrip("https://"))
print(website.lstrip('/:pthw.'))
print(emir.strip('en.com'))
print(emir.lower())
print(emir.upper())
print(emir.title())
print(emir.count("e"))
print(emir.startswith("e")) #true or false
print(emir.endswith(".com"))
print(emir.find('d')) #index numarası
print(emir.isalpha()) #hepsi harf mi
print(alfabe.isalpha())
print("Emir".center(25)) #emir kelimesini merkeze al sağdan soldan totalde 25 hane olsun. .centerın ikinci parametsine boşluk yerine gelecek karakter seçimi yapılır.
print("Emir".rjust(25)) #sağa yaslar.
print("Emir".ljust(25))
print(course.replace(" ","-" ))
"""



"""

#listelerrrrrr

list = [1,2,3,4,5]
list2 = [6,7,8,9,10]
print(list+list2)
print(len(list+list2))
print(list[1])
kisi1=["emir",22]
kisi2=["didem",20]
kisiler=[kisi1,kisi2]

print(kisiler[1])
print(kisi2)
print(kisi1[0])
print(kisiler[0][0])
"""

"""
araba=["bmw","mercedes","opel","mazda"]
print(len(araba))
print(araba[0],araba[3])
print(araba[3].replace("mazda","toyota"))
print(araba.__contains__("mercedes")) #mercedes listenin bir üyesi mi ?
print("mercedes" in araba) #mercedes listenin bir üyesi mi ?
print(araba[-2])
print(araba[0:3])
araba[2:4]=["toyota","renault"]
print(araba)
result=araba + ["audi","nissan"]
print(result)
del araba[3]
print(araba)
print(araba[::-1]) #tersten yazdırır -1

"""



"""
numbers = [1,2,3,4,5,65,7,8,9,10]
letters = ['a','b','c','d','e']
numbers[5]=6
numbers.append(55) #55 sayısını diziye ekle
numbers.insert(3,78) #dizinin istediğin indexine istediğin sayıyı ekle.
numbers.pop() #son eklenen eleman olan 78 i diziden siler.parametre olarak indexi baz alır.
numbers.remove(4) #elemanı siler.
letters.sort() # alfabetik olarak sıralama yapar.
letters.remove("c") # elemanı siler.

print(letters)
print(numbers)
print(min(numbers))
numbers.reverse() #diziyi ters cevirme
print(numbers)
print(min(letters))
print(max(numbers))
print(max(letters))
"""



"""
names = ["Ali","Yagmur","Hakan","Deniz"]
years =[1998,2000,1998,1987]
#1
names.append("Cenk")
print(names)
#2
names.insert(0,"Sena")
print(names)
#3
print(names.index("Deniz"))
#4
names.remove("Deniz")
print(names)
#5
print("Ali" in names)
#6
names.reverse()
print(names)
#7
names.sort()
print(names)
#8
years.sort()
years.reverse()
print(years)
#9
str="Chevrolet,Dacia"
str.split(",")
print(str)

#10
print(max(years))
print(min(years))
#11
print(years.count(1998))
#12
print(years.clear())

#13 kullanıcıdan alınan 3 adet marka bilgisini bir dizide tut.
markalar=[]
for i in range(0,3):
    marka=input("Bir marka Giriniz :")
    markalar.append(marka)
print(markalar)
"""

"""
#Değişebilir dizi : LİST
#Değiştirilemez dizi : TUPLE

tupleornek =("ali","veli",5)
print(tupleornek)
print(tupleornek.count("ali"))
print(tupleornek.index("veli"))
print(tupleornek.index(5))


"""




"""
#Dictionary List Özelliklleri

plakalar = {"kayseri":38, "istanbul":34, "erzurum":25}
print(plakalar["kayseri"])
print(plakalar)
plakalar["ankara"] =6
print(plakalar)

plakalar["mersin"]=33
print(plakalar)
plakalar["hatay"]=31
print(plakalar)

"""


"""

ogrenciler={
    "":{
        "ad":"",
        "soyad":"",
        "telefon":""

    },
    "":{
        "ad":"",
        "soyad":"",
        "telefon":""
    },
    "":{
        "ad":"",
        "soyad":"",
        "telefon":""
    },
}
"""




"""

ogrenciler={}

for i in range(0,3):
    ogrNo =input("Ögrenci No : ")
    ogrAdi =input("Ögrenci Adi : ")
    ogrSoyadi =input("Ögrenci Soyadi : ")
    ogrTel =input("Telefon : ")
    ogrenciler.update({
        ogrNo:{
            "isim":   ogrAdi,
        "soyisim":  ogrSoyadi,
        "telefon":  ogrTel,
    }


    })
print(ogrenciler)

"""


"""
#set listeleri


meyveler = {"elma","muz","karpuz"}

for i in meyveler:
    print(i)


meyveler.add("Mandalina")
print(meyveler)
meyveler.update(["karpuz","çilek","ananas"])
print(meyveler)
meyveler.remove("Mandalina")
print(meyveler)
meyveler.discard("karpuz")
print(meyveler)
meyveler.pop() # ilk elemanı sildi
print(meyveler)
"""





"""
x,y,z = 2,5,107

numbers =1,5,7,10,6

# sayi1=int(input("Bir Sayi Giriniz : "))
# sayi2=int(input("Bir Sayi Daha Giriniz : "))
# print((sayi1*sayi2)-(x+y+z))

print(y//x)
print((x+y+z)%3)
print(y**x)

x, *y, z = numbers
print(x,y,z)
print(z**3)
print(y[0]+y[1]+y[2])

"""



"""
# sayi1=int(input("Bir Sayi Giriniz : "))
# sayi2=int(input("Bir Başka Sayi Giriniz : "))
# print(sayi1>sayi2)
# print(sayi1<sayi2)


vize=int(input("Vize Notunu Giriniz : "))
vize2=int(input("Vize 2  Notunu Giriniz : "))
final=int(input("Final Notunu Giriniz : "))
ort=(vize+vize2)/2*0.6+final*0.4
if(ort>=50):
    print("Ortalama {0} dersten geçtiniz.".format(ort))
else:
    print("Ortalama {0} dersten kaldınız.".format(ort))
    
    
    
sayi=int(input("Bir Sayi Giriniz : "))
deger=(sayi%2==0)
print(f"Sayi Cifttir {deger}")

tekcift=(sayi>0)
print(f"Sayi Pozitiftir {tekcift} ")

email=input("Email giriniz : ")
parola=input("Parola Giriniz :")
emailCheck="email.emir"
parolaCheck="parola.emir"

checkmail=(email==emailCheck)
checkparola=(parola==parolaCheck)

print(f"Email Doğrulama ... {checkmail},Parola Doğrulama ... {checkparola}")


"""

"""

sayi=int(input("Bir Sayi Giriniz:"))
if(0<sayi<100):
    print(f"{sayi} 0-100 Arasındadir")
else:
    print(f"{sayi} 0-100 Arasında Değildir.")

if(sayi%2==0 and sayi>0):
    print(f"{sayi} pozitif çift sayıdır.")
"""




urunler=[]
urunSayisi=int(input("Kaç Adet Ürün Eklenecek : "))
i=0
while(i<urunSayisi):
    urunAdi=input("Ürün Adı Giriniz: ")
    urunFiyati=input("Ürün Fiyatı Giriniz: ")
    urunler.append({
         "Ürün Adı":urunAdi,
         "Ürün Fiyatı":urunFiyati,
     })
    i+=1

print(urunler)





















