raw_data = input("").split(" ")
a = int(raw_data[0])
b = int(raw_data[1])
c = int(raw_data[2])

print((a + b) % c)
print((a % c + b % c) % c)
print((a * b) % c)
print((a % c * b % c) % c)
