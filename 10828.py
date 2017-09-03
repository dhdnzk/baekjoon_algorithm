class Stack():

    def __init__(self):
        self.ary = []

    def push(self, x):
        self.ary.append(x)
        return

    def pop(self):
        if self.ary.__len__() <= 0:
            print("-1")
        else:
            print(self.ary.pop(self.ary.__len__() - 1))
        return

    def size(self):
        print(self.ary.__len__());
        return

    def empty(self):
        if self.ary.__len__() == 0:
            print(1)
        else:
            print(0)
        return

    def top(self):
        if self.ary.__len__() <= 0:
            print("-1")

        else:
            print(self.ary[self.ary.__len__() - 1])

    def decoder(self, x):
        decoded_ary = x.split(' ')

        if decoded_ary[0] == "push":
            self.push(int(decoded_ary[1]))
            return

        if decoded_ary[0] == "pop":
            self.pop()
            return

        if decoded_ary[0] == "size":
            self.size()
            return
        if decoded_ary[0] == "empty":
            self.empty()
            return

        if decoded_ary[0] == "top":
            self.top()
            return

count = int(input(""))

stack = Stack()

for i in range(0, count):
    stack.decoder(input(""))
