# Push 6 in the bottom of the stack

# Before : 1 2 3 4 5
# After  : 6 1 2 3 4 5 

from collections import deque

def Push_Bottom(s,item):
    if (len(s)==0):
        s.append(item)
        return
    top = s.pop()
    Push_Bottom(s,item)
    s.append(top)

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

print(stack)

Push_Bottom(stack,6)

print(stack)