class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length += 1

    def __str__(self):
        temp = self.head
        result = ''
        while temp:
            result += temp.vale
            if temp.next:
                result += '->'
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

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.head = new_node
            self.head = new_node
        if index < 0 or index > self.length:
            return False
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def tranverse(self):
        temp = self.head
        while temp:
            return temp.value
        temp = temp.next

    def search(self, target):
        temp = self.head
        index = 0
        while temp:
            if temp.val == target:
                index += 1
                return temp
            temp = temp.next
            index += 1
        return -1
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        return temp.value
    
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        return temp
    
    def pop_last(self):
        if self.length == 0:
            return None
        temp = self.head
        popped_node = self.tail
        self.tail = temp
        self.tail.next = None

    def remove(self, index):
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop_last()
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        self.length -= 1
        return popped_node
    

    def remove_element(self, target):
        temp = self.head
        while temp and temp.next:
            if temp.next.value == target:
                temp.next = temp.next.next
                self.length -= 1
            else:
                temp = temp.next

    def palindrome(self):
        if not self.head or self.head.next:
            return False
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        first_half, second_half = self.head, prev
        while second_half:
            if first_half.value != second_half.value:
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True