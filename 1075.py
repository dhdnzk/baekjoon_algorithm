def calc(n, f):
    base_num = n - n % 100

    for i in range(0, f):
        target_num = base_num + i
        if target_num % f == 0:
            return i


n = int(input())
f = int(input())

print("%02d" % calc(n, f))
