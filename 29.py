class Stack:
    def __init__(self):
        self.stack=[]
        self.top=-1

    def push(self,item):
        self.stack.append(item)
        self.top +=1

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            print("Popped",self.stack.pop())
            self.top-=1
    def peep(self):
        if self.top==-1:
            print("Stack is empty")
        else:
            print("Stack elements:",self.stack)
s=Stack()
while True:
    print("\n Menu 1.Push 2.Pop 3.Peep 4.Print 5.Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        val=int(input("Enter value to PUSH"))
        s.push(val)
    elif ch==2:
        s.pop()
    elif ch==3:
        s.peep()
    elif ch==4:
        s.print_stack()
    elif ch==5:
        break
    else:
        print("Invalid choice")









        
