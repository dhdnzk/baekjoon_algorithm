board = []

for i in range(0, 8):
    board.append(list(input()))


counter = 0

for i in range(0, 8):
    for j in range(0, 8):
        if (i + j) % 2 == 0:
            if board[i][j] == 'F':
                counter += 1

print(counter)
