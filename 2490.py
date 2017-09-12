for i in range(0, 3):
    li = [int(i) for i in input().split(" ")]
    result = 0
    for num in li:
        result += num
    if result == 0:
        print("D")
    if result == 1:
        print("C")
    elif result == 2:
        print("B")
    elif result == 3:
        print("A")
    elif result == 4:
        print("E")

