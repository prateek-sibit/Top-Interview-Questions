'''

Problem : Suppose we have a standard linked list. 
Construct an in-place 
(without extra memory) algorithm thats 
able to find the middle node!

Solutions : 
1) Naive solution : we iterate through the list and then stop when node with 
    index count//2 is reached
2) Using Two pointers : we can use two pointers to get to the middle in O(N)
    
'''

class Node():
    
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList():
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    # O(1) time complexity 
    def insertStart(self, data):
        self.size += 1
        newNode = Node(data)
        
        if self.head == None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    
    # O(N) time complexity
    def remove(self, data):
        
        if self.head is None:
            return
        
        self.size -= 1
        
        currentNode = self.head
        previousNode = None
        
        while currentNode.data != data:
            previousNode, currentNode = currentNode, currentNode.nextNode
        
        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode 
    
    # O(1) time complexity
    def size1(self):
        return self.size
    
    # O(N) time complexity
    def insertEnd(self, data):

        self.size += 1
        newNode = Node(data)
        actualNode = self.head
        
        while(actualNode.nextNode is not None):
            actualNode = actualNode.nextNode
            
        actualNode.nextNode = newNode
        newNode.nextNode = None
    
    def traverseList(self):
        
        actualNode = self.head
        
        while actualNode is not None:
            print('{0}'.format(actualNode.data))
            actualNode = actualNode.nextNode
    
    # O(N)
    # Method 1
    def findMiddleNode(self):
        
        actualNode = self.head
        size = self.size1()
        
        for iteration in range(0,size//2):
            actualNode = actualNode.nextNode
                
        return actualNode
    
    # O(N)
    # Method 2
    def findMiddleNodePointer(self):
            
        slow_pointer = self.head
        fast_pointer = self.head
        
        while fast_pointer.nextNode and fast_pointer.nextNode.nextNode:
            fast_pointer = fast_pointer.nextNode.nextNode
            slow_pointer = slow_pointer.nextNode
        
        return slow_pointer
    
# Testing
linked_list = LinkedList()
linked_list.insertStart(12)
linked_list.insertStart(122)    
linked_list.insertStart(3)
linked_list.insertStart(5)
linked_list.insertStart(21)
linked_list.insertStart(99)
linked_list.insertStart(15)
linked_list.insertStart(18)
linked_list.insertStart(20)

midNode = linked_list.findMiddleNode()
print('Middle Node : ',midNode.data)

midNodePointer = linked_list.findMiddleNodePointer()
print('Middle Node : ',midNodePointer.data)