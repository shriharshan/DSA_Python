class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def mergeTwoLists(self, list1, list2):
        dummy = Node(-1)
        current = dummy
        while list1 and list2:
            if list1.value < list2.value:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next
        
        
        
l1 = Node(1)
l1.next = Node(3)
l1.next.next = Node(5)

l2 = Node(2)
l2.next = Node(4)
l2.next.next = Node(6)

solution = LinkedList()
merged = solution.mergeTwoLists(l1, l2)

# Print merged list
while merged:
    print(merged.value, end=" -> ")
    merged = merged.next
