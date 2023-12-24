meyveler = {"elma", "muz", "karpuz"}

for meyve in meyveler:
    print(meyve)

meyveler.add("Mandalina")
print(meyveler)
meyveler.update(["karpuz", "çilek", "ananas"])
print(meyveler)
meyveler.remove("Mandalina")
print(meyveler)
meyveler.discard("karpuz")
print(meyveler)
meyveler.pop()
print(meyveler)
