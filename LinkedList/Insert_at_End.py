class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value) #--------> O(1) to create a node
        if self.head is None: #---------> O(1) to check if the node is None
            self.head = new_node # O(1) setting head and tail of a node
            self.tail = new_node #
        else:
            self.tail.next = new_node # O(1) setting next pointer of tail to the new node 
            self.tail = new_node
        self.length += 1 # ---------> O(1) increasing the length by 1

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
print(new_linked_list.tail.value)

# The total complexity to perform append operation to insert in the end is O(1) 