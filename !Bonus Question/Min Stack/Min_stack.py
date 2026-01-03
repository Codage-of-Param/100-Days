'''Min Stack 

    Time complexity = O(1)
    Space complexity = O(n) because of push operation
    
'''

class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minVal = None
        
    def push(self,val):
        if not self.stack:
            self.stack.append(val)
            self.minVal = val
            
        elif (val < self.minVal):
            encoded = 2*val - self.minVal
            self.stack.append(encoded)
            self.minVal = val
        
        else:
            self.stack.append(val)
        
    def pop(self):
        top = self.stack.pop()
        if (top < self.minVal):
            self.minVal = 2*self.minVal - top
        
        
    def top(self):
        if (self.stack[-1] < self.minVal):
            return self.minVal
        else:
            return self.stack[-1]
        
    def getMin(self):
        return self.minVal
    
minStack1 = MinStack()

minStack1.push(-2)
minStack1.push(0)
minStack1.push(-3)

min1 = minStack1.getMin()
print(f"Minimum value of stack is {min1}")

minStack1.pop()

top1 = minStack1.top()
print(f"Top element of stack is {top1}")

min2 = minStack1.getMin()
print(f"Minimum value of stack after pop element 1 time is {min2}")
