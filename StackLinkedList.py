#Link list implementation of Stack


class Node:

#Initialization
    def __init__(self,x):
        self.data = x
        self.next = None


class Stack:

    def __init__(self):
        self.top = None

    def push(self,x):
        new_node = Node(x) #Newnode
        new_node.next = self.top  # Assign newnode.next to self.top value
        self.top = new_node  # assign the new node value as top


    def pop(self):
        self.top = self.top.next

    def top_element(self):
        return self.top.data

    def display(self):
       print("top",end=("->"))
       p = self.top
       while p:
           print(p.data, end="->")
           p = p.next
       print("None")



stk = Stack()

stk.push(10)
stk.push(20)
stk.push(15)
stk.display()
stk.pop()
stk.display()
print(f"Top element : {stk.top_element()}")