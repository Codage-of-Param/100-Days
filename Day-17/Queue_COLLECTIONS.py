from collections import deque

Queue = deque()

# Enqueue : TC = O(1)
Queue.append(1)
Queue.append(2)
Queue.append(3)
Queue.append(4)
Queue.append(5)

print(Queue)

# Dequeue : TC = O(1)
Queue.popleft()
Queue.popleft()

print(Queue)

# Enqueue (Left) : TC = O(1)
Queue.appendleft(2)

print(Queue)

# Dequeue (Right) : TC = O(1)
Queue.pop()

print(Queue)

# Peek (Front) Which is default: TC = O(1)
front = Queue[0]
print(f"Front element of Queue is {front}")

# Peek (Rear) : TC = O(1)
rear = Queue[-1]
print(f"Rear element of Queue is {rear}")

# Size : TC = O(1)
size = len(Queue)
print(f"Size of the queue is {size}")

# isEmpty: TC = O(1)
if (size==0):
    print("Queue is empty!")
else:
    print("Queue is Non-empty!")