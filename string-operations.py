website = "http://www.emirdagdelen.com/"

emir = "eMiRhaNdaGdelen.com"
alfabe = "abcdefg"


print(website[7:10])
print(website.lstrip("http://"))
print(website.lstrip('/:pthw.'))
print(emir.strip('en.com'))
print(emir.lower())
print(emir.upper())
print(emir.title())
print(emir.count("e"))
print(emir.startswith("e"))  # True veya False
print(emir.endswith(".com"))
print(emir.find('d'))  # index numarası
print(emir.isalpha())  # hepsi harf mi
print(alfabe.isalpha())
print("Emir".center(25))  # emir kelimesini merkeze al, sağdan soldan toplamda 25 karakter olsun
print("Emir".rjust(25))  # sağa yaslar
print("Emir".ljust(25))  # sola yaslar

