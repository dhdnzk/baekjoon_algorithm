class Editor:

    def __init__(self, string):
        self.cursor = len(string)
        self.str = list(string)
        self.processed_order = ""

    def decoder(self, data):
        self.processed_order = data.split(" ")

        if self.processed_order[0].upper() == "L":
            self.cursor_left()

        if self.processed_order[0].upper() == "D":
            self.cursor_right()

        if self.processed_order[0].upper() == "B":
            self.del_left_side_letter()

        if self.processed_order[0].upper() == "P":
            self.append_letter_to_left_side(self.processed_order[1])

    def cursor_left(self):
        if self.cursor > 0:
            self.cursor -= 1
        elif self.cursor <= 0:
            self.cursor = 0

    def cursor_right(self):
        if self.cursor < len(self.str):
            self.cursor += 1
        elif self.cursor >= len(self.str):
            self.cursor = len(self.str)

    def del_left_side_letter(self):
        if self.cursor <= 0:
            return
        self.str.pop(self.cursor - 1)
        self.cursor -= 1

    def append_letter_to_left_side(self, letter):
        self.str.insert(self.cursor, letter)
        self.cursor += 1

    def print_str(self):
        self.str = "".join(self.str)
        print(self.str)


raw_data = input("")

operation_count = input("")

editor = Editor(raw_data)

for i in range(0, int(operation_count)):
    command = input("")
    editor.decoder(command)

editor.print_str()
