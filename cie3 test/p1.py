class Node:
    def __init__(self):
        self.data = None 
        self.next = None 
class queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node()
        new_node.data = data
        if self.front is None:
           self.front = new_node
           self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    
    
    def fornt(self):
        if self.front is None:
            return None
        return self.front.data 
        
    def is_empty(self):
        return self.front is None
        
    def dequeue(self):
        if self.front is None:
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return data
    
       


    


    
        



