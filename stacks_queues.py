#####################
# Stacks and Queues #
#####################

# In software engineering, stacks and queues are fundamental data structures used for organizing and manipulating data. 
# Stacks follow the Last In, First Out (LIFO) principle, resembling a stack of plates. 
# Queues, on the other hand, adhere to the First In, First Out (FIFO) principle, similar to waiting in line for a service. 
# Understanding these concepts is essential for efficient programming and problem-solving.

# Stack - Last In First Out - is_empty, push, pop, peek, size
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('Cannot pop from an empty stack')

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('Cannot peek from an empty stack')

    def size(self):
        return len(self.items)


# BrowserHistory - Stack

# print("Welcome to the browser")
# browser_history = Stack()
# url = input('Enter URL or "quit": ')
# while url != 'quit':
#     if url == 'back':
#         browser_history.pop()
#     else:
#         browser_history.push(url)

#     current_page = browser_history.peek()
#     print("Currently viewing: ", current_page)
#     url = input('Enter URL, "back", or "quit": ')

# Queue - First In First Out - is_empty, peek, size, enqueue, dequeue

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError('Cannot dequeue from an empty queue')

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError('Cannot peek from an empty queue')

    def size(self):
        return len(self.items)


class Printer:
    def __init__(self):
        self.jobs = Queue()

    def add_to_queue(self, document):
        self.jobs.enqueue(document)
        print(f"Document '{document}' has been added to the jobs")

    def print_document(self):
        if not self.jobs.is_empty():
            document = self.jobs.dequeue()
            print(f"Printing document: {document}")
        else:
            print("Print queue is empty")


my_printer = Printer()

my_printer.add_to_queue('Document 1')
my_printer.add_to_queue('Document 2')

my_printer.print_document() # Prints "Document 1"

my_printer.add_to_queue('Document 3')

my_printer.print_document() # Prints "Document 2"
my_printer.add_to_queue('Document 4')
my_printer.print_document() # Prints "Document 3"
my_printer.print_document() # Prints "Document 4"
