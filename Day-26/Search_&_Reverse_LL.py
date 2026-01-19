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
        
    def search(self, FindingValue):
        temp = self.head

        while temp is not None:
            if (temp.data == FindingValue):
                return True        
            temp = temp.next
        return False
    
    def reverse(self): # 3 variables, 4 steps 
        Prev = None
        Current = self.head
        
        while(Current != None):
            Next = Current.next
            Current.next = Prev
            Prev = Current
            Current = Next
        
        self.tail = self.head 
        self.head = Prev
    
LL1 = LinkedList()

LL1.add_first(1)
LL1.add_last(3)
LL1.add_middle(1,2)
LL1.add_last(4) 
LL1.add_middle(4,5) 

print(LL1.printLL())

print("----------")

answer = LL1.search(3)
print("Searched Element is present?, (True/False) : ", answer)

print("----------")

print("Reverse a Linked list:")
LL1.reverse()
print(LL1.printLL())

print("----------")