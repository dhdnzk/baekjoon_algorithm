raw_data = list(input())
counter = 0

idx = 0
while True:
    if idx >= raw_data.__len__():
        break
    if raw_data[idx] == 'c':
        if idx + 1 < raw_data.__len__():
            if raw_data[idx + 1] == "=" or raw_data[idx + 1] == '-':
                raw_data.pop(idx)
                raw_data.pop(idx)
                counter += 1
            else:
                raw_data.pop(idx)
                counter += 1

    elif raw_data[idx] == 'd':
        if idx + 1 < raw_data.__len__():
            if raw_data[idx + 1] == "-":
                raw_data.pop(idx)
                raw_data.pop(idx)
                counter += 1

            elif raw_data[idx + 1] == "z":
                if idx + 2 < raw_data.__len__():
                    if raw_data[idx + 2] == "=":
                        raw_data.pop(idx)
                        raw_data.pop(idx)
                        raw_data.pop(idx)
                        counter += 1
                    else:
                        raw_data.pop(idx)
                        counter += 1

            else:
                raw_data.pop(idx)
                counter += 1

    elif raw_data[idx] == 'l':
        if idx + 1 < raw_data.__len__():
            if raw_data[idx + 1] == "j":
                raw_data.pop(idx)
                raw_data.pop(idx)
                counter += 1
            else:
                raw_data.pop(idx)
                counter += 1

    elif raw_data[idx] == 'n':
        if idx + 1 < raw_data.__len__():
            if raw_data[idx + 1] == "j":
                raw_data.pop(idx)
                raw_data.pop(idx)
                counter += 1
            else:
                raw_data.pop(idx)
                counter += 1

    elif raw_data[idx] == 's':
        if idx + 1 < raw_data.__len__():
            if raw_data[idx + 1] == "=":
                raw_data.pop(idx)
                raw_data.pop(idx)
                counter += 1
            else:
                raw_data.pop(idx)
                counter += 1

    elif raw_data[idx] == 'z':
        if idx + 1 < raw_data.__len__():
            if raw_data[idx + 1] == "=":
                raw_data.pop(idx)
                raw_data.pop(idx)
                counter += 1
            else:
                raw_data.pop(idx)
                counter += 1

    else:
        raw_data.pop(idx)
        counter += 1

print(counter)



