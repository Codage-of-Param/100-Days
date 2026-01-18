from collections import deque

class LinkedList:
    def __init__(self):
        self.ll = deque()

    def insert_head(self, data):
        self.ll.appendleft(data)

    def insert_tail(self, data):
        self.ll.append(data)

    def delete_head(self):
        if self.ll:
            return self.ll.popleft()
        return None

    def delete_tail(self):
        if self.ll:
            return self.ll.pop()
        return None

    def search(self, value):
        return value in self.ll

    def remove(self, value):
        if value in self.ll:
            self.ll.remove(value)

    def display(self):
        print(list(self.ll))

    def length(self):
        return len(self.ll)

ll = LinkedList()
ll.insert_head(10)
ll.insert_tail(20)
ll.insert_tail(30)

ll.display()      
ll.delete_head()
ll.display()      