# Queue implementation using LIST (FIFO)

# enqueue, dequeue, peek, isEmpty, size

def enqueue(q): 
    n = int(input("How many elements you want to Enque? => "))
    
    for i in range(n):
        elem = input(f"Enter an element {i+1} : " )
        q.append(elem)
        
    return q

def dequeue(Queue): # TC = O(n)
    if not (isEmpty(Queue)):
        Queue.pop(0)
        return Queue
    else:
        print("\nQueue is empty!")

def peek(Queue): # Front element 
    if not (isEmpty(Queue)):
        return Queue[0]
    else:
        print("\nQueue is empty!")

def isEmpty(Queue):
    if len(Queue)==0:
        return True
    else:
        return False
    
def size(Queue):
    return len(Queue)
     
q = []

Queue = enqueue(q)
print(Queue)

dequeue(Queue)
print(Queue)
 
element = peek(Queue)
print(f"\n Front element is {element}")

is_ = isEmpty(Queue)
print(f"\n Queues is Empty? => {is_}")

sizze = size(Queue)
print(f"\n Size of Queue  => {sizze}")