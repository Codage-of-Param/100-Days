'''Min Stack [Approach-2]

    With two stacks (Main_stack & Min_stack)
        - Main_stack for values
        - Min_stack for minimum values till position
        
    Time complexity = O(1) 
    Space complexity = O(n)
'''

class MinStack:
    
    def __init__(self):
        self.Main_Stack = []
        self.Min_Stack = []
        
    def push(self, val:int):
        
        if not (self.Main_Stack and self.Min_Stack):
            self.Main_Stack.append(val)
            self.Min_Stack.append(val)
            
        if  (val < self.Min_Stack[-1]):
            self.Main_Stack.append(val)
            self.Min_Stack.append(val)
            
        elif (val > self.Min_Stack[-1]):
            self.Main_Stack.append(val)
            self.Min_Stack.append(self.Min_Stack[-1])
    
    def pop(self):
        return self.Main_Stack.pop() and self.Min_Stack.pop()
    
    
    def getMin(self):
        return self.Min_Stack[-1]
    
minStack2 = MinStack()

minStack2.push(-2)
minStack2.push(10)
minStack2.push(11)
minStack2.push(2)
minStack2.push(3)
minStack2.push(15)

minStack2.pop()
minStack2.pop()

minimum = minStack2.getMin()
print(f"Minimum value of Main stack is {minimum}")