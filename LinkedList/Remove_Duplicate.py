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

    def prepand(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    def remove_duplicated(self):
        if self.head is None:
            return None
        current = self.head
        node_values = set()
        node_values.add(current.value)
        while current.next:
            if current.next.value in node_values:
                current.next = current.next.next
                self.length -= 1
            else:
                node_values.add(current.next.value)
                current = current.next
        self.tail = current.next
        
        
        

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(30)
print(new_linked_list)
print(new_linked_list.remove_duplicated())
print(new_linked_list)