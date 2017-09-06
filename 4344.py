count = int(input())

for i in range(0, count):
    ary = input().split(" ")
    ary = [int(i) for i in ary[1:]]

    student_counter = 0
    average = 0

    for i in ary:
        average += i

    average = average / ary.__len__()

    for i in ary:
        if i > average:
            student_counter += 1

    percentage = student_counter / ary.__len__()
    print("{0:.3f}%".format(student_counter / ary.__len__() * 100))

