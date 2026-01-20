# Question from : https://www.geeksforgeeks.org/dsa/delete-nth-node-from-the-end-of-the-given-linked-list/

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def Remove_nth_Node_from_end(self, n):  # O(1) Time complexity
        
        # Use formula Size-n+1
        
        if(n == self.size):
            self.head = self.head.next # basically remove first method
            return
        
        # For, size - n
        i = 1
        idxToFind = self.size - n
        prev = self.head
        
        while(i < idxToFind):
            prev = prev.next
            i+=1
            
        prev.next = prev.next.next
        return 
        
    def add_first(self, data)->Node:   # O(1) Time complexity
        NewNode = Node(data)
        
        if (self.head==None):
            self.head=self.tail=NewNode
            self.size+=1
            return
        
        NewNode.next = self.head
        self.head = NewNode
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
            print(temp.data,end=" → ")
            temp = temp.next
        
        
llist1 = LinkedList()
llist1.add_first(2)
llist1.add_first(1)
llist1.add_first(0)
llist1.add_last(6)
llist1.add_last(4)


print(llist1.printLL())
print("Size : ",llist1.size)

print("---------------")

# llist1.Remove_nth_Node_from_end(5) # 5th node from end
# print(llist1.printLL())

# llist1.Remove_nth_Node_from_end(3) # 3rd node from end
# print(llist1.printLL())

llist1.Remove_nth_Node_from_end(1) # First node from end
print(llist1.printLL())