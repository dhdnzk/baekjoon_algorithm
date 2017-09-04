def decoder(alphabet, letter, idx):

    if letter == "a":
        if alphabet[0] == -1:
            alphabet[0] = idx
    elif letter == "b":
        if alphabet[1] == -1:
            alphabet[1] = idx
    elif letter == "c":
        if alphabet[2] == -1:
            alphabet[2] = idx
    elif letter == "d":
        if alphabet[3] == -1:
            alphabet[3] = idx
    elif letter == "e":
        if alphabet[4] == -1:
            alphabet[4] = idx
    elif letter == "f":
        if alphabet[5] == -1:
            alphabet[5] = idx
    elif letter == "g":
        if alphabet[6] == -1:
            alphabet[6] = idx
    elif letter == "h":
        if alphabet[7] == -1:
            alphabet[7] = idx
    elif letter == "i":
        if alphabet[8] == -1:
            alphabet[8] = idx
    elif letter == "j":
        if alphabet[9] == -1:
            alphabet[9] = idx
    elif letter == "k":
        if alphabet[10] == -1:
            alphabet[10] = idx
    elif letter == "l":
        if alphabet[11] == -1:
            alphabet[11] = idx
    elif letter == "m":
        if alphabet[12] == -1:
            alphabet[12] = idx
    elif letter == "n":
        if alphabet[13] == -1:
            alphabet[13] = idx
    elif letter == "o":
        if alphabet[14] == -1:
            alphabet[14] = idx
    elif letter == "p":
        if alphabet[15] == -1:
            alphabet[15] = idx
    elif letter == "q":
        if alphabet[16] == -1:
            alphabet[16] = idx
    elif letter == "r":
        if alphabet[17] == -1:
            alphabet[17] = idx
    elif letter == "s":
        if alphabet[18] == -1:
            alphabet[18] = idx
    elif letter == "t":
        if alphabet[19] == -1:
            alphabet[19] = idx
    elif letter == "u":
        if alphabet[20] == -1:
            alphabet[20] = idx
    elif letter == "v":
        if alphabet[21] == -1:
            alphabet[21] = idx
    elif letter == "w":
        if alphabet[22] == -1:
            alphabet[22] = idx
    elif letter == "x":
        if alphabet[23] == -1:
            alphabet[23] = idx
    elif letter == "y":
        if alphabet[24] == -1:
            alphabet[24] = idx
    elif letter == "z":
        if alphabet[25] == -1:
            alphabet[25] = idx

alphabet = [-1 for i in range(0, 26)]
data = input("")
data = list(data)

for i in range(0, len(data)):
    letter = str(data.pop(0))

    decoder(alphabet, letter, i)

for i in range(0, alphabet.__len__()):
    print(alphabet[i], end=" ")
