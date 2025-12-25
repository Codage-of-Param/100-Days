from collections import deque

stack = deque()

stack.append(10)
stack.append(20)

top = stack[-1]
print(top)

print(stack.pop())

'''
Pros: Explicit intent, safe and fast
Cons: Slightly more verbose than list
'''

'''
The deque is better because list pop(0) is O(n), while deque operations are O(1).
'''