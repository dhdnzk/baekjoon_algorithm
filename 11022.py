import re

count = input("");
ary = list();

for i in range(0, int(count)):

    raw_data = input("");
    numbers = re.findall("\d+", raw_data);
    a = int(numbers[0]);
    b = int(numbers[1]);
    ary.append([a, b, a + b]);

num = 0;
for i in ary:
    num +=1;
    print("Case #" + str(num) + ": " + str(i[0]) + " + " + str(i[1]) + " = " + str(i[2]));

