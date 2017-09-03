count = input("");

a = list();

for i in range(0, int(count)):
    raw_data = input("");
    a.append(int(raw_data[0]) + int(raw_data[2]));

for i in a:
    print(i);

