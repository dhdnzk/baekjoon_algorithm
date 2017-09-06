num_of_objects = input()

subject_list = input().split(" ")
subject_list = [int(i) for i in subject_list]

max_score = 0
for i in subject_list:
    if max_score < i:
        max_score = i

for i in range(0, subject_list.__len__()):
    subject_list[i] = subject_list[i] / max_score * 100

sum = 0
for i in subject_list:
    sum += i

average = sum / subject_list.__len__()

print('%.2f' % average)
