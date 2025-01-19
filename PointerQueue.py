

class Node : #Initialization of node
    def __init__(self,d):
        self.data = d
        self.next = None


class QueueItems:
    def __init__(self):
        #initialization of front and rear pointers
        self.front  = None
        self.rear = None

    def enqu(self,x):
        new_node = Node(x)

        # If the queue is empty, both the rear and front point to the new node
        if self.front is None:
           self.front = self.rear = new_node

        #if the queue is not empty, point the rear node to the new node
        else:
            self.rear.next = new_node #Link the current rear to the new node
            self.rear = new_node #Update the rear pointer to the new Node

    def dequ(self):
       self.front = self.front.next

       if self.front is None:
           self.rear = None

    def displayfront(self):
        return self.front.data

    def displayrear(self):
        return self.rear.data
    def display(self):
        print("Front",end ="->")
        p = self.front
        while p:
            print(p.data, end="->")
            p=p.next
        print("Rear")


q = QueueItems()
print("Before Dequeue")
q.enqu(10)
q.enqu(20)
q.enqu(30)
q.enqu(40)
q.display()
print(f'Front: {q.displayfront()}')
print(f'Rear: {q.displayrear()}')
q.dequ()
print("After Dequeue")
q.display()
print(f'Front: {q.displayfront()}')
print(f'Rear: {q.displayrear()}')





