words = input().split(" ")
space_counter = 0

for i in words:
    if i == "":
        space_counter += 1

print(words.__len__() - space_counter)

