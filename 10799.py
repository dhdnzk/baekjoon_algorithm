def calc_basic_stick_num(x):

    lazer_count = 0
    end_parenthesis_count = 0

    for i in range(0, len(x)):
        if x[i] == ')':
            end_parenthesis_count += 1
            if x[i-1] == '(':
                lazer_count += 1

    return end_parenthesis_count - lazer_count


def calc_cut_blocks(x):

    start_parenthesis = 0
    end_parenthesis = 0
    added_block_count = 0

    for i in range(0, len(x)):
        if x[i] == "(":
            start_parenthesis += 1
        else:
            end_parenthesis += 1
            if x[i-1] == "(":
                added_block_count += (start_parenthesis - end_parenthesis)

    return added_block_count


raw_data = input("")
print(calc_basic_stick_num(raw_data) + calc_cut_blocks(raw_data))


