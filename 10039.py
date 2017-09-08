score_list = list()
for i in range(0, 5):
    score = int(input())
    score_list.append(score) if score > 40 else score_list.append(40)

total_score = 0
for i in score_list:
    total_score += i

average = int(total_score / score_list.__len__())

print(average)
