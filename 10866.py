# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

class Deque:
    def __init__(self):
        self.ary = []

    def push_front(self, data):
        self.ary.insert(0, int(data))

    def push_back(self, data):
        self.ary.insert(self.ary.__len__(), int(data))

    def pop_front(self):
        if self.ary.__len__() == 0:
            print("-1")
        else:
            print(self.ary.pop(0))

    def pop_back(self):
        if self.ary.__len__() == 0:
            print("-1")

        else:
            print(self.ary.pop(self.ary.__len__() - 1))

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

        if processed_data[0].lower() == "push_front":
            self.push_front(int(processed_data[1]))

        elif processed_data[0].lower() == "push_back":
            self.push_back(int(processed_data[1]))

        elif processed_data[0].lower() == "pop_front":
            self.pop_front()

        elif processed_data[0].lower() == "pop_back":
            self.pop_back()

        elif processed_data[0].lower() == "size":
            self.size()

        elif processed_data[0].lower() == "empty":
            self.empty()

        elif processed_data[0].lower() == "front":
            self.front()

        elif processed_data[0].lower() == "back":
            self.back()


deque = Deque()
count = int(input(""))
for i in range(0, count):
    deque.decoder(input(""))
