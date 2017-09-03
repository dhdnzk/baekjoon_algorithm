class Editor:

    processed_order = ""
    str = ""
    cursor = 0

    def __init__(self, string):
        self.cursor = len(string) + 1
        self.str = string

    def decoder(self, data):
        self.processed_order = data.split(" ")

        if self.processed_order[0].upper() == "L":
            self.cursor_left()
            return

        if self.processed_order[0].upper() == "D":
            self.cursor_right()
            return

        if self.processed_order[0].upper() == "B":
            self.del_left_side_letter()
            return

        if self.processed_order[0].upper() == "P":
            self.append_letter_to_left_side(self.processed_order[1])
            return

    def cursor_left(self):
        if self.cursor > 0:
            self.cursor -= 1

    def cursor_right(self):
        if self.cursor < len(self.str):
            self.cursor += 1

    def del_left_side_letter(self):

        tmp_str = list(self.str)
        tmp_str.remove(self.cursor)
        self.str = "".join(tmp_str)
        print(self.str)

    def append_letter_to_left_side(self, letter):

        tmp_str = list(self.str)
        tmp_str.insert(self.cursor, letter)
        self.str = "".join(tmp_str)
        print(self.str)


raw_data = input("")

operation_count = input("")

editor = Editor(raw_data)

for i in range(0, int(operation_count)):
    editor.decoder(input(""))


