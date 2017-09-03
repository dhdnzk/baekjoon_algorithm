import re

count = input("");
ary = list();

for i in range(0, int(count)):

    raw_data = input("");
    numbers = re.findall("\d+", raw_data);
    a = int(numbers[0]);
    b = int(numbers[1]);
    ary.append(a + b);

for i in ary:
    print(i);

