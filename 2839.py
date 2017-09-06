n = int(input())

five_count = 0
three_count = 0
rest = n

while (3 * three_count) <= n:
    if rest % 5 == 0:
        five_count = int(rest / 5)
        rest = 0
        break
    rest -= 3
    three_count += 1

if rest != 0:
    print(-1)
else:
    print(five_count + three_count)


