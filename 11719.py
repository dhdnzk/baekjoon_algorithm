buffer = list()
for i in range(0, 100):
    try:
        tmp_buffer = input()
        buffer.append(tmp_buffer)
    except EOFError:
        break

for i in buffer:
    print(i)
