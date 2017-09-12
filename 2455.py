counter = 0
max_counter = 0
for i in range(0, 4):
    data = input().split(" ")
    counter -= int(data[0])
    counter += int(data[1])
    if max_counter < counter:
        max_counter = counter

print(max_counter)
