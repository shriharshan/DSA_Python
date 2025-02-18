class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
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
        
    #isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
        
    #push
    def push(self, value):
        if self.isFull():
            return "Stack is full"
        else:
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
        
    #delete
    def delete(self):
        self.list = None
        

customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())

customStack.push(10)
customStack.push(20)
customStack.push(30)

print(customStack)