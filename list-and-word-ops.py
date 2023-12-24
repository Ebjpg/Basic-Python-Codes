names = ["Ali", "Yagmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

# 1
names.append("Cenk")
print(names)

# 2
names.insert(0, "Sena")
print(names)

# 3
print(names.index("Deniz"))

# 4
names.remove("Deniz")
print(names)

# 5
print("Ali" in names)

# 6
names.reverse()
print(names)

# 7
names.sort()
print(names)

# 8
years.sort()
years.reverse()
print(years)

# 9
str = "Chevrolet,Dacia"
print(str.split(","))

# 10
print(max(years))
print(min(years))

# 11
print(years.count(1998))

# 12
print(years.clear())
