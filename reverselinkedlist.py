'''

Problem : Construct an in-place algorithm to reverse a linked list!

1) Naive solution : we consider all the nodes one by one then
construct another linked list in reverse order
Problem : It has O(N) memory complexity so it is not in-place

2) Using pointers : we can achieve an inplace algorithm that has 
O(N) linear running time complexity

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
        
        print('Linked List Traversal')
        
        actualNode = self.head
        
        while actualNode is not None:
            print('{0}'.format(actualNode.data))
            actualNode = actualNode.nextNode
    
    # O(N) Time Complexity
    def reverse(self):
        
        current_node = self.head
        previous_node = None
        next_node = None
        
        while current_node is not None:
            next_node = current_node.nextNode
            current_node.nextNode = previous_node
            previous_node = current_node
            current_node = next_node
        
        self.head = previous_node

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

linked_list.traverseList()
linked_list.reverse()
linked_list.traverseList()


