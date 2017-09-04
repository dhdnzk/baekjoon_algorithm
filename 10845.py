class Queue:
    def __init__(self):
        self.ary = []

    def push(self, data):
        self.ary.insert(self.ary.__len__(), int(data))

    def pop(self):
        if self.ary.__len__() == 0:
            print("-1")
        else:
            print(self.ary.pop(0))

    def size(self):
        print(self.ary.__len__())

    def empty(self):
        if self.ary.__len__() == 0:
            print("1")
        else:
            print("0")

    def front(self):
        if self.ary.__len__() == 0:
            print("-1")
        else:
            print(self.ary[0])

    def back(self):
        if self.ary.__len__() == 0:
            print("-1")
        else:
            print(self.ary[self.ary.__len__() - 1])

    def decoder(self, raw_data):
        processed_data = raw_data.split(" ")

        if processed_data[0].lower() == "push":
            self.push(int(processed_data[1]))

        elif processed_data[0].lower() == "pop":
            self.pop()

        elif processed_data[0].lower() == "size":
            self.size()

        elif processed_data[0].lower() == "empty":
            self.empty()

        elif processed_data[0].lower() == "front":
            self.front()

        elif processed_data[0].lower() == "back":
            self.back()


queue = Queue()
count = int(input(""))
for i in range(0, count):
    queue.decoder(input(""))
