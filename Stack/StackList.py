class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    #push
    def push(self, value):
        self.list.append(value)
        return "the element has been pushed"
    
    #pop
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list.pop()
        
    #peek
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list[-1]
        
    #Delete
    def delete(self):
        self.list = None
    
customStack = Stack()
customStack.push(10)
customStack.push(20)
customStack.push(30)
print(customStack.peek())
