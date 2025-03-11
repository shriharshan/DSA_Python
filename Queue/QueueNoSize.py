class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    # isEmpty
    def isEmpty(self):
        return self.items == []
    
    #enqueue
    def enqueue(self, value):
        self.items.append(value)
        return "the element has been enqueued"
    
    #dequeue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items.pop(0)
        
    #peek
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items[0]
        
    #delete
    def delete(self):
        self.items = None


customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue.dequeue())
print(customQueue.peek())
print(customQueue)