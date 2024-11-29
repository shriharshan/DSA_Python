class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        temp = self.head
        result = ''
        while temp:
            result += str(temp.value)
            if temp.next is not None:
                result += ' -> '
            temp = temp.next
        return result
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        
    def traverse(self):
        current = self.head
        while current:
            return current.value
        current = current.next
        
    def search(self, target):
        temp = self.head
        while temp:
            if temp.value == target:
                return True
            temp = temp.next
        return -1
        
    def get(self, index):
        if index < 0 or index > self.length:
            return False
        temp = self.head
        while temp:
            for _ in range(index):
                temp = temp.next
            return temp
        
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        
        
        
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)
print(new_linked_list.set(2, 50))
print(new_linked_list)