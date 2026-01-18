class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def add_first(self, data)->Node:   # O(1) Time complexity
        NewNode = Node(data)
        
        if (self.head==None):
            self.head=self.tail=NewNode
            self.size+=1
            return
        
        NewNode.next = self.head
        self.head = NewNode
        self.size+=1
        
    def add_middle(self,index,data):
        NewNode = Node(data)
        temp = self.head
        
        if (index==0):
            self.add_first(data)
            return
        
        i = 0
        
        while(i < (index-1)):
            temp = temp.next
            i+=1
        NewNode.next = temp.next
        temp.next = NewNode
        self.size+=1
        
    def add_last(self,data)->Node:   # O(1) Time complexity
        NewNode = Node(data)
        
        if (self.head==None):
            self.head = self.tail = NewNode
            return
        
        self.tail.next = NewNode
        self.tail = NewNode
        self.size+=1
        
    def printLL(self):
        temp = (self.head)
        while(temp!=None):
            print(temp.data)
            temp = temp.next
            
    def remove_first(self):
        
        if(self.size == 0):
            print("Linked-List is empty!")
            return None
            
        elif(self.size == 1):
            value = self.head.data
            self.head = self.tail = None
            
            self.size-=1
            return value
        
        value = self.head.data
        self.head = self.head.next
        self.size-=1
        return value
    
    def remove_last(self):
        
        temp = (self.head)
        while(temp.next.next!=None):
            temp = temp.next
            
        self.tail = temp
        temp.next = None
        
        self.size-=1
        
    def remove_idx(self, index):
        temp = self.head
        i = 0
        
        while(i < (index-1)):
            temp = temp.next
            i+=1
            
        temp.next = temp.next.next
        self.size-=1
        
        
llist1 = LinkedList()
llist1.add_first(2)
llist1.add_first(4)

print(llist1.printLL())
print("Size : ",llist1.size)

print("---------------")

llist1.add_last(1)
l2 = llist1.printLL()
print(l2)

print("---------------")

llist1.add_middle(2,7)
print(llist1.printLL())
print("Size : ",llist1.size)

print("---------------")

llist1.remove_first()
print(llist1.printLL())

print("---------------")

llist1.remove_last()
print(llist1.printLL())

print("---------------")

llist1.remove_idx(1)
print(llist1.printLL())

print("---------------")

print("Size : ",llist1.size)

print("---------------")