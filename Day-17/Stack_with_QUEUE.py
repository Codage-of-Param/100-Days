# Question From : https://leetcode.com/problems/implement-stack-using-queues/description/

class myStack:
    
    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)        

    def pop(self) -> int:
        if not self.empty():
            return self.items.pop(-1)

    def top(self) -> int:
        if not self.empty():
            return self.items[-1]

    def empty(self) -> bool:
        if (len(self.items) == 0):
            return True
        else:
            return False
        
obj = myStack()
obj.push(1)
obj.push(2)
obj.push(3)

param_2 = obj.pop()
print(param_2)

param_3 = obj.top()
print(param_3)

param_4 = obj.empty()
print(param_4)

'''
OUTPUT:

3
2
False

'''
