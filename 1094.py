target_num = int(input())
bin_num = bin(target_num)[2:]
answer = 0

for i in bin_num:
    answer += int(i)

print(answer)
