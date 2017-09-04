alphabet = "abcdefghijklmnopqrstuvwxyz"
raw_data = input("")
encrypted_data = ""

for i in range(0, len(raw_data)):
    capital_flag = False
    if raw_data[i].isalpha():

        if raw_data[i].isupper():
            capital_flag = True

        idx = (alphabet.index(raw_data[i].lower()) + 13) % 26

        if capital_flag:
            encrypted_data += alphabet[idx].upper()
        else:
            encrypted_data += alphabet[idx]

    else:
        encrypted_data += raw_data[i]

print(encrypted_data)
