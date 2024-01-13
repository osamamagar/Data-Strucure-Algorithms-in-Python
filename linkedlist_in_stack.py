#stack in Data Structure 
#Last In First Out (LIFO)
#LinkedList (non contiguous, dynamic size,can be done more efficiently 
# since it involves updating pointers, and no shifting of elements is required.
# Access Time not best than array because 
# complexity is n or O(n), Lower cache locality than Array )



class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def append(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node

        else:
            current = self.head
            while current.next is not None :
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


my_list = LinkedList()

my_list.append(10)
my_list.append(20)
my_list.append(30)

print("Linked List:")
my_list.display()





