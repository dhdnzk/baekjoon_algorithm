cups = [True, False, False]

for i in range(0, int(input())):
    idxes = input().split(" ")
    idxes = [int(i) for i in idxes]
    tmp = cups[idxes[0] - 1]
    cups[idxes[0] - 1] = cups[idxes[1] - 1]
    cups[idxes[1] - 1] = tmp

for i in range(0, cups.__len__()):
    if cups[i]:
        print(i + 1)
