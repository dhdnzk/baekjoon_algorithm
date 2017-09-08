def group_word_checker(word):

    dictionary = {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
        'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
        'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0
    }

    for idx in range(0, word.__len__()):
        if idx == 0:
            dictionary[word[idx].upper()] += 1
        elif idx > 0:
            if word[idx] != word[idx - 1]:
                dictionary[word[idx].upper()] += 1

    for idx in dictionary.values():
        if idx > 1:
            return False

    return True


group_word_counter = 0

for i in range(0, int(input())):
    if group_word_checker(str(input())):
        group_word_counter += 1

print(group_word_counter)

