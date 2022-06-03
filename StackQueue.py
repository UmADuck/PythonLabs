class Node:
    def __init__(self,  real: int, imaginary: int) -> None:
        self.real = real
        self.imaginary = imaginary
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None
        self.sum = None
        self.size = 0
        self.last_node_real = 0
        self.last_node_imaginary = 0


    def isempty(self) -> None:
        if self.head == None:
            return True
        else:
            return False

    def push(self, real: int, imaginary: int) -> None:

        if self.head == None:
            self.head=Node(real, imaginary)

        else:
            newnode = Node(real, imaginary)
            newnode.next = self.head
            self.head = newnode
            self.last_node_imaginary = newnode.next.imaginary
            self.last_node_real = newnode.next.real

    def pop(self):

        if self.isempty():
            return None

        else:
            poppernode = self.head
            self.head = self.head.next
            poppernode.next = None
            return (poppernode.real, poppernode.imaginary)


    def peek(self) -> None:

        if self.isempty():
            return None

        else:
            print (F"Top element is: ({self.head.real} + ({self.head.imaginary}i))\n")
        return
    def display(self) -> None:

        iternode = self.head
        if self.isempty():
            print("Stack underflow")

        else:

            while(iternode != None):
                    self.size+=1
                    print(f"({iternode.real} + ({iternode.imaginary}i))" + "->", end = " ")
                    iternode = iternode.next
            print(f"None, size ={self.size} \n")
            self.size = 0
            return

    def summary(self):

        print(F"({self.last_node_real} + ({self.head.real})) + ({self.last_node_imaginary} + ({self.head.imaginary}))i"+
        f" = {self.last_node_real + self.head.real} + ({self.last_node_imaginary + self.head.imaginary}i)\n")
        return

    def difference(self):

        print(F"({self.last_node_real} - ({self.head.real})) - ({self.last_node_imaginary} - ({self.head.imaginary}))i"+
        f" = {self.last_node_real - self.head.real} - ({self.last_node_imaginary - self.head.imaginary}i)\n")
        return

    def find_the_location(self, real: int, imaginary: int):

        iternode = self.head

        while(iternode != None):
            self.size+=1
            if (iternode.real == real):
                if(iternode.imaginary == imaginary):
                    print(f"The place of complex number ({real} + ({imaginary}i): {self.size}\n")
            iternode = iternode.next
        self.size = 0
        return

MyStack = Stack()

MyStack.push(1, 5)
MyStack.push(-2, 4)
MyStack.push(5,-8)
MyStack.push(-1, -7)

MyStack.display()

MyStack.find_the_location(-2, 4)

MyStack.summary()
MyStack.difference()

MyStack.peek()

MyStack.pop()
MyStack.pop()

MyStack.display()

MyStack.peek()