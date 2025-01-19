
class QueueList: #Queue FIFO

    def __init__(self):
        self.queueItems = [] #Initialize array

    def push(self,x):
        self.queueItems.append(x) #adds the element to the back (or rear) of the queue

    def pop(self):  #removes the first element
        self.queueItems.pop(0) #Kaya siya (0) because and ipopop is yung first index palagi FIFO

    def front(self):
        return self.queueItems[0]

    def rear(self): #or you can use self.queueItems[len(self.queueItems) -1]
        return  self.queueItems[-1] #to access the last element

    def display(self):
        print(self.queueItems)

q = QueueList()

q.push(10)
q.push(3)
q.push(40)
q.display()
print(f'Front: {q.front()}')
print(f'Rear: {q.rear()}')
q.pop()
q.display()
print(f'Front: {q.front()}')
print(f'Rear: {q.rear()}')
