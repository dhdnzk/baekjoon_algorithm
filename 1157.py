user_input = input().upper()

dictionary = {

    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0,
    'J': 0,
    'K': 0,
    'L': 0,
    'M': 0,
    'N': 0,
    'O': 0,
    'P': 0,
    'Q': 0,
    'R': 0,
    'S': 0,
    'T': 0,
    'U': 0,
    'V': 0,
    'W': 0,
    'X': 0,
    'Y': 0,
    'Z': 0

}


for i in user_input:
    dictionary[i] += 1

max_alphabet = ""
max_num = 0

for i in dictionary.items():
    if max_num == i[1]:
        if i[1] != 0:
            max_alphabet = "?"
    if max_num < i[1]:
        max_num = i[1]
        max_alphabet = i[0]

print(max_alphabet)
