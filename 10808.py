def decoder(alphabet, letter):
    if letter == "a":
        alphabet[0] += 1
    elif letter == "b":
        alphabet[1] += 1
    elif letter == "c":
        alphabet[2] += 1
    elif letter == "d":
        alphabet[3] += 1
    elif letter == "e":
        alphabet[4] += 1
    elif letter == "f":
        alphabet[5] += 1
    elif letter == "g":
        alphabet[6] += 1
    elif letter == "h":
        alphabet[7] += 1
    elif letter == "i":
        alphabet[8] += 1
    elif letter == "j":
        alphabet[9] += 1
    elif letter == "k":
        alphabet[10] += 1
    elif letter == "l":
        alphabet[11] += 1
    elif letter == "m":
        alphabet[12] += 1
    elif letter == "n":
        alphabet[13] += 1
    elif letter == "o":
        alphabet[14] += 1
    elif letter == "p":
        alphabet[15] += 1
    elif letter == "q":
        alphabet[16] += 1
    elif letter == "r":
        alphabet[17] += 1
    elif letter == "s":
        alphabet[18] += 1
    elif letter == "t":
        alphabet[19] += 1
    elif letter == "u":
        alphabet[20] += 1
    elif letter == "v":
        alphabet[21] += 1
    elif letter == "w":
        alphabet[22] += 1
    elif letter == "x":
        alphabet[23] += 1
    elif letter == "y":
        alphabet[24] += 1
    elif letter == "z":
        alphabet[25] += 1

alphabet = [0 for i in range(0, 26)]
data = input("")
data = list(data)

for i in range(0, len(data)):
    letter = str(data.pop(0))

    decoder(alphabet, letter)

for i in range(0, alphabet.__len__()):
    print(alphabet[i], end=" ")
