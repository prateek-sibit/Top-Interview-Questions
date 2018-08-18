# Linked List Implementation in python

class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.nextNode = None
    
class LinkedList(object):
    
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
    
    # O(N) time complexity ~ Not Good
    def size2(self):
    
        actualNode = self.head
        size = 0
        
        while(actualNode != None):
            size += 1
            actualNode = actualNode.nextNode
        return size
    
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
            
# Testing the Linked List
            
linked_list = LinkedList()
linked_list.insertStart(12)
linked_list.insertStart(122)
linked_list.insertStart(3)
linked_list.insertEnd(31)

linked_list.traverseList()
print('Size of the linked List : ',linked_list.size1())

linked_list.remove(31)
linked_list.remove(12)
linked_list.remove(122)
linked_list.remove(3)

print('Size of the linked list : ',linked_list.size1())