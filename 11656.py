raw_data = input("")
ary = []
for i in range(0, len(raw_data)):
    ary.append(raw_data[i:])

ary = sorted(ary)
for i in ary:
    print(i)

