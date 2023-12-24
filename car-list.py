arabalar = ["bmw", "mercedes", "opel", "mazda"]
print(len(arabalar))
print(arabalar[0], arabalar[3])
print(arabalar[3].replace("mazda", "toyota"))
print("mercedes" in arabalar)
print(arabalar[-2])
print(arabalar[0:3])
arabalar[2:4] = ["toyota", "renault"]
print(arabalar)
result = arabalar + ["audi", "nissan"]
print(result)
del arabalar[3]
print(arabalar)
print(arabalar[::-1])
