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
            if temp.next:
                result += ' -> '
            temp = temp.next
        return result
        
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    def insert(self, index, value):
        new_node = Node(value)
        temp = self.head
        if index < 0 or index > self.length:
            return False
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            
    def traverse(self):
        temp = self.head
        while temp:
            return temp.value
            temp = temp.next
            
    def search(self, target):
        temp = self.head
        index = 0
        while temp:
            if temp.value == target:
                return index
            temp = temp.next
        return -1
        
    def get(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
        return True
    
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
        
    def pop_last(self):
        popped_node = self.tail
        temp = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            while temp is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
            self.length -= 1
        return popped_node
        
    def remove(self, index):
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop_last()
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
        
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
        
        
        
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)
print(new_linked_list.delete_all())
print(new_linked_list)