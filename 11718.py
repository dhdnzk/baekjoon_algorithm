while True:
    try:
        str = input()
        print(str, end="")
    except EOFError:
        break
