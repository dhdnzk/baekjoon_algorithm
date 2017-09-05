
raw_data = input("").split(" ")
big_num = raw_data[0] if raw_data[0] >= raw_data[1] else raw_data[1]
small_num = int(raw_data[0] if raw_data[0] < raw_data[1] else raw_data[1])
big_num = int(big_num)
small_num = int(small_num)

GCD = 1
LCM = big_num

for i in range(1, small_num + 1):
    if big_num % i == 0 and small_num % i == 0:
        GCD = i

while True:
    if LCM % big_num == 0 and LCM % small_num == 0:
        break
    LCM += 1

print(GCD)
print(LCM)
