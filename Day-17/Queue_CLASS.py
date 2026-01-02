# Queue implementation using CLASS (FIFO)

# enqueue, dequeue, peek, isEmpty, size

class Queues:
    
    def __init__(self):
        self.queue = []
    
    def enqueue(self,elem): # TC : O(1)
        self.queue.append(elem)
        
    def dequeue(self): # TC : O(n)
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            print("\n Queue is Empty!")
    
    def peek(self):  # TC : O(1)
        if not self.isEmpty():
            front = self.queue[0]
            return front
        else:
            print("\n Queue is Empty!")
    
    def isEmpty(self):  # TC : O(1)
        if (self.size() == 0):
            return True
        else:
            return False
        
    def size(self):  # TC : O(1)
        return len(self.queue)

    
Q1 = Queues()

Q1.enqueue(2)
Q1.enqueue(1)
Q1.enqueue(3)

print(f"Queue is {Q1.queue}")

Removed = Q1.dequeue()
print(f"Removed front element: {Removed}")

front = Q1.peek()
print(f"Front is {front}")

size = Q1.size()
print(f"Size of Queue is {size}")

is_ = Q1.isEmpty()
print(f"Queue is Empty? => {is_}")

print(f"Now, The Queue is {Q1.queue}")