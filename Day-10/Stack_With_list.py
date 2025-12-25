# STACK from SCRATCH 

class stack:
    
    def __init__ (self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
            
    def is_empty(self):
        if (self.size()==0):
            return True
        else:
            return False
    
    def size(self):
        return len(self.items)
    
    def __repr__(self): # representation of an object
        return f"Stack({self.items})"
    
s = stack()

s.push(1)
s.push(2)
s.push(3)

print(s.pop())#3

print(s.peek()) #2

print(f"Size of the stack is {s.size()}")

print(s.__repr__()) # representation in form of list

'''
Pros: Simple, built-in, efficient for append/pop at the end
Cons: No explicit stack interface (discipline is by convention)
'''