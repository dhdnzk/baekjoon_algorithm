def score_calculator(ox_string):
    score_of_this_prob = 1
    total_score = 0

    for idx in range(0, ox_string.__len__()):
        if ox_string[idx].upper() == "O":
            total_score += score_of_this_prob
            score_of_this_prob += 1
        else:
            score_of_this_prob = 1

    return total_score


counter = int(input())

for i in range(0, counter):
    user_input = input()
    print(score_calculator(user_input))
