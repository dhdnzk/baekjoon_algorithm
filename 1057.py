raw_data = input().split(" ")
table = [int(0) for i in range(0, int(raw_data[0]))]
table[int(raw_data[1]) - 1] = 1
table[int(raw_data[2]) - 1] = 1

counter = 1
idx = 0
cur_table = []
while True:

    player1 = 0
    player2 = 0

    if table.__len__() > 0:
        player1 = table.pop(0)
    if table.__len__() > 0:
        player2 = table.pop(0)

    if player1 == player2 == 1:
        break
    elif player1 == 1 or player2 == 1:
        cur_table.append(1)
    else:
        cur_table.append(0)

    if table.__len__() == 0:
        table = cur_table
        cur_table = []
        counter += 1

print(counter)
