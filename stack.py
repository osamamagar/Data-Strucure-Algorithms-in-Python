#stack in Data Structure 
#Last In First Out (LIFO)


class Stack():
    
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,value):
        self.items.append(value)
        print(f"{value} was append on stack")



    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None  
        else:
            popped = self.items.pop()
            print(f"{popped} popped from the stack")
            return popped



    def peek(self):
        if self.is_empty():
            return 'Stack is empty'
        else:   
            return self.items[-1]


my_stack = Stack()

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print("Top element:", my_stack.peek())

popped_element = my_stack.pop()
if popped_element is not None:
    print("Popped element:", popped_element)

print("Top element:", my_stack.peek())


popped_element = my_stack.pop()
if popped_element is not None:
    print("Popped element:", popped_element)

print("Top element:", my_stack.peek())
print("Is the stack empty?", "Yes" if my_stack.is_empty() else "No")

popped_element = my_stack.pop()
if popped_element is not None:
    print("Popped element:", popped_element)

print("Top element:", my_stack.peek())


print("Is the stack empty?", "Yes" if my_stack.is_empty() else "No")

        
    

