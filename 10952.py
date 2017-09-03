import re

while(True):

    raw_data = input("");
    numbers = re.findall("\d+", raw_data);
    a = int(numbers[0]);
    b = int(numbers[1]);
    if(a == b == 0):
        break;
    result = a + b;
    print(result);
