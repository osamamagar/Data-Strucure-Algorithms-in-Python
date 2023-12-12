

class Task:
    def __init__(self, description):
        self.description = description
        self.next = None



class Todo:
    def __init__(self):
        self.head = None

    def add_task(self, description):
        new_task = Task(description)
        if self.head is None:
            self.head = new_task
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_task


    def display_tasks(self):
        current = self.head
        if current is None :
            print("Nothing to display")

        else:
            print("Task List: ")
            while current is not None:
                print(f"- {current.description}")
                current = current.next

    
    def remove_task(self, description):
        current = self.head
        previous = None

        while current is not None and current.description == description :
            previous = current
            current = current.next

        if current is None :
            print(f"Task '{description}' not found.")

        elif previous is None :
            self.head = current.next
            print(f"Task '{description}' removed.")
        
        else:
            previous.next = current.next
            print(f"Task '{description}' removed.")


my_todo_list = Todo()

my_todo_list.add_task("Complete programming assignment")
my_todo_list.add_task("Buy groceries")
my_todo_list.add_task("Read a chapter of a book")

my_todo_list.display_tasks()

my_todo_list.remove_task("Buy groceries")

my_todo_list.display_tasks()
