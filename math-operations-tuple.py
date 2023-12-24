x, y, z = 2, 5, 107
numbers = 1, 5, 7, 10, 6

print(y // x)
print((x + y + z) % 3)
print(y ** x)

x, *y, z = numbers
print(x, y, z)
print(z ** 3)
print(y[0] + y[1] + y[2])
