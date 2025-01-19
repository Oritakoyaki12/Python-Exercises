#Stack Implementation using Array

class Stack:

    def __init__(self):
        self.stack = [] #Defining array


    def push(self,x):
        self.stack.append(x)

    def pop(self):
        self.stack.pop() #initially last index yung default na tinatanggal

    def top(self):
        return self.stack[len(self.stack)-1]

    def display(self):
        print(self.stack)



stk = Stack()

stk.push(30)
stk.push(20)
stk.push(10)
stk.display()
stk.pop()
stk.display()


print(f"Top Element: {stk.top()}")


