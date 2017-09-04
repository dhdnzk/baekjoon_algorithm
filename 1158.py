raw_data = input("")
raw_data = raw_data.split(" ")
n = int(raw_data[0])
m = int(raw_data[1])
ary = list(range(1, int(n) + 1))
cursor = 0

print("<", end="")
for i in range(0, n):
    cursor = (cursor + m - 1) % ary.__len__()
    print(ary.pop(cursor), end="")
    if ary.__len__() != 0:
        print(", ", end="")
print(">", end="")


