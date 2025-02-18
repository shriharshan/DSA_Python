class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode.value
            curNode = curNode.next
    
class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linked_list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.linked_list.head == None:
            return True
        else:
            return False
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.linked_list.head
        self.linked_list.head = new_node

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            popped_value = self.linked_list.head.value
            self.linked_list.head = self.linked_list.head.next
            return popped_value
        
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.linked_list.head.value
        
    def delete(self):
        self.linked_list.head = None

customStack = Stack() 
customStack.push(10)
customStack.push(20)
customStack.push(30)
print(customStack)
print("-------------")
print(customStack.pop())
print("-------------")
print(customStack)