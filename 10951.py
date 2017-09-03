import re

while(True):

    raw_data = input("");
    numbers = re.findall("\d+", raw_data);
    a = int(numbers[0]);
    b = int(numbers[1]);
    if(a < 0 or a > 10 or b < 0 or b > 10 ):
        break;
    result = a + b;
    print(result);
