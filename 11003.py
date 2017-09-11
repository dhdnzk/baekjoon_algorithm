raw_data = input().split(" ")

n = int(raw_data[0])
l = int(raw_data[1])
d = list()

ary = [int(i) for i in input().split(" ")]

for i in range(1, n + 1):
    startidx = i - l if i - l > 0 else 0

    sub_str = ary[startidx:i]
    d.append(min(sub_str))

for i in d:
    print(i, end=" ")

