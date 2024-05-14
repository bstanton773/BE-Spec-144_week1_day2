################
# Linked Lists #
################

# Linked lists are fundamental data structures in computer science used for storing and managing collections of data. Unlike python lists, 
# linked lists do not require contiguous memory allocation, allowing for dynamic memory allocation and efficient insertion and 
# deletion operations. Linked lists consist of nodes, each containing a data element and a reference (or pointer) to the next 
# node in the sequence. This flexibility makes linked lists suitable for various applications, such as implementing stacks, queues,
# and managing dynamic lists of items, making them an essential concept for aspiring software developers to understand.


# 2 Classes - A Node Class and a Linked List Class

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<Node|{self.value}>"


class SinglyLinkedList:
    def __init__(self):
        # set the .head attribute to point to None to start (an empty Linked List)
        self.head = None

    # Method to add a new node to the beginning of the Linked List
    def push(self, new_value): # O(1) - Constant Time
        # Create a new node with the value passed in to the method
        new_node = Node(new_value)
        # Set the new node's .next attribute to be the front of the linked list (aka the head)
        new_node.next = self.head
        # Set the new node to be the beginning of the list (aka the head)
        self.head = new_node

    # Method to add a new node to the end of the Linked List
    def append(self, new_value): # O(n) - Linear Time
        # Create a new node with the value pass in to the method
        new_node = Node(new_value)
        # If the linked list is empty
        if self.head is None:
            # Set the new node as the first element in the list
            self.head = new_node
        # If not empty
        else:
            # Start at the first node
            current_node = self.head
            # Keep moving until the current_node has no next 
            while current_node.next is not None:
                # Move on to the next node
                current_node = current_node.next
            # Once current_node.next is None, set it to be the new node
            current_node.next = new_node

    # Method to print out all of the nodes in the linked list in order
    def traverse(self): # O(n) - Linear Time 
        print('Linked List Elements:')
        # Start at the beginning of the list
        print('head\n | \n V')
        current = self.head
        # While current is a node and not None
        while current:
            # Print the node with an arrow
            print(current, end=' -> ')
            # Move on to the next node in the linked list
            current = current.next
        # Print None at the end
        print(None)

    # Method to get a node by value
    def get_node(self, value_to_get): # O(n) - Linear
        # Start with the beginning
        node_to_check = self.head
        # While node_to_check is a node
        while node_to_check:
            # Check if this is the node we are looking for
            if node_to_check.value == value_to_get:
                # we foun the node, return it
                return node_to_check
            # if not, move to the next node
            node_to_check = node_to_check.next
        # If the node_to_check becomes None, we know the value is not in the linked list
        return None

    # Method to insert a new node into the linked list after a certain node (by value)
    def insert_after(self, prev_value, new_value): # O(n) - Linear
        # Get the previos node by value
        prev_node = self.get_node(prev_value)
        # Make sure that the prev_node exists
        if prev_node is None:
            print(f"{prev_value} is not in the linked list")
        else:
            # Create a new node with the new value
            new_node = Node(new_value)
            # point the new_node's .next to the prev_node's .next
            new_node.next = prev_node.next
            # point the prev_node's .next at the new node
            prev_node.next = new_node

    # Method to remove a node from the Linked List
    def remove(self, value_to_remove):
        # Check if the list is empty
        if self.head is None:
            print('List is empty, nothing to remove')
            return
        # If the first node is the node we are trying to removing
        if self.head.value == value_to_remove:
            # Set the .head attribute to be the next node
            self.head = self.head.next
            return
        # Start at the first node
        current_node = self.head
        # While the current node has a next node
        while current_node.next:
            # If the next node is the one we are trying to remove
            if current_node.next.value == value_to_remove:
                # Set the current node's next to be its next's next node
                current_node.next = current_node.next.next
                return
            # If not, move on to the next node
            current_node = current_node.next
        # If we get to the end of the Linked List without returning, the node was never there
        print(f"{value_to_remove} is not in this Linked List.")


if __name__ == "__main__":
    months = SinglyLinkedList()
    months.append('July')
    months.append('August')
    months.append('September')
    months.push('May')
    months.push('April')
    months.append('Codember')
    months.push('March')
    months.append('October')
    months.push('February')
    months.insert_after('May', 'June')
    months.push('January')
    months.append('December')
    months.insert_after('October', 'November')
    months.remove('Codember')

    months.traverse()


# DoublyLinkedList
# Similar to SinglyLinked, except the node has a 3rd attribute .prev that points to the node before it in the LinkedList

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<Node|{self.value}>"


class DoublyLinkedList:
    def __init__(self):
        # set the .head attribute to point to None to start (an empty Linked List)
        self.head = None

    # Method to add a new node to the beginning of the Linked List
    def push(self, new_value): # O(1) - Constant Time
        # Create a new node with the value passed in to the method
        new_node = Node(new_value)
        # If there is a node at the head
        if self.head:
            # Set the head's previous node to be the new node
            self.head.prev = new_node
        # Set the new node's .next attribute to be the front of the linked list (aka the head)
        new_node.next = self.head
        # Set the new node to be the beginning of the list (aka the head)
        self.head = new_node

    # Method to add a new node to the end of the Linked List
    def append(self, new_value): # O(n) - Linear Time
        # Create a new node with the value pass in to the method
        new_node = Node(new_value)
        # If the linked list is empty
        if self.head is None:
            # Set the new node as the first element in the list
            self.head = new_node
        # If not empty
        else:
            # Start at the first node
            current_node = self.head
            # Keep moving until the current_node has no next 
            while current_node.next is not None:
                # Move on to the next node
                current_node = current_node.next
            # Once current_node.next is None, set it to be the new node
            current_node.next = new_node
            # Set the new_node's previous to be the current node
            new_node.prev = current_node

    # Method to print out all of the nodes in the linked list in order
    def traverse(self): # O(n) - Linear Time 
        print('Linked List Elements:')
        # Start at the beginning of the list
        print('head\n | \n V')
        current = self.head
        # While current is a node and not None
        while current:
            # Print the node with an arrow
            print(current, end=' <--> ')
            # Move on to the next node in the linked list
            current = current.next
        # Print None at the end
        print(None)

    # Method to get a node by value
    def get_node(self, value_to_get): # O(n) - Linear
        # Start with the beginning
        node_to_check = self.head
        # While node_to_check is a node
        while node_to_check:
            # Check if this is the node we are looking for
            if node_to_check.value == value_to_get:
                # we foun the node, return it
                return node_to_check
            # if not, move to the next node
            node_to_check = node_to_check.next
        # If the node_to_check becomes None, we know the value is not in the linked list
        return None

    # Method to insert a new node into the linked list after a certain node (by value)
    def insert_after(self, prev_value, new_value): # O(n) - Linear
        # Get the previos node by value
        prev_node = self.get_node(prev_value)
        # Make sure that the prev_node exists
        if prev_node is None:
            print(f"{prev_value} is not in the linked list")
        else:
            # Create a new node with the new value
            new_node = Node(new_value)
            # point the new_node's .next to the prev_node's .next
            new_node.next = prev_node.next
            # if the previous node has a next
            if prev_node.next:
                # Set the previous node's next .prev to be the new node
                prev_node.next.prev = new_node
            # point the prev_node's .next at the new node
            prev_node.next = new_node
            # new node's .prev to the previous node
            new_node.prev = prev_node

    # Method to remove a node from the Linked List
    def remove(self, value_to_remove):
        # Check if the list is empty
        if self.head is None:
            print('List is empty, nothing to remove')
            return
        # If the first node is the node we are trying to removing
        if self.head.value == value_to_remove:
            # Set the .head attribute to be the next node
            self.head = self.head.next
            # If the new head is a node
            if self.head:
                self.head.prev = None
            return
        # Start at the first node
        current_node = self.head
        # While the current node is not None
        while current_node:
            # If the current node is the one we are trying to remove
            if current_node.value == value_to_remove:
                # Adjust the pointers
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                return
            # If not, move on to the next node
            current_node = current_node.next
        # If we get to the end of the Linked List without returning, the node was never there
        print(f"{value_to_remove} is not in this Linked List.")


days = DoublyLinkedList()
days.push('Monday')
days.append('Thursday')
days.append('Saturday')
days.push('Sunday')
days.insert_after('Monday', 'Tuesday')
days.insert_after('Tuesday', 'Wednesday')
days.insert_after('Thursday', 'Friday')

days.remove('Sunday')
days.remove('Wednesday')

days.traverse()



# Practical Use Case

# Playlist Management System

class Song:
    def __init__(self, title, artist, duration, genre):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.artist}\nDuration: {self.duration}\nGenre: {self.genre}"

class Node:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None

class PlaylistManager:
    def __init__(self, name):
        self.name = name
        self.head = None
        self.current_song = None

    def add_song(self, title, artist, duration, genre):
        # Create a new Song instance with the args
        new_song = Song(title, artist, duration, genre)
        # Create a node with the Song
        new_node = Node(new_song)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node
            new_node.prev = node

    def remove_song(self, title):
        if self.head is None:
            print(f"The playlist '{self.name}' is empty")
            return
        # If the first node is the node we are trying to removing
        if self.head.song.title == title:
            # Set the .head attribute to be the next node
            self.head = self.head.next
            # If the new head is a node
            if self.head:
                self.head.prev = None
            return
        # Start at the first node
        current_node = self.head
        # While the current node is not None
        while current_node:
            # If the current node is the one we are trying to remove
            if current_node.song.title == title:
                # Adjust the pointers
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                return
            # If not, move on to the next node
            current_node = current_node.next
        # If we get to the end of the Linked List without returning, the node was never there
        print(f"{title} is not in the '{self.name}' playlist.")

    def play_next(self):
        # If there is no current song
        if self.current_song is None:
            # Set the current song to the first song in the playlist
            self.current_song = self.head
        # if there is
        else:
            # Set the current song to the next song
            self.current_song = self.current_song.next
        # Make sure that the new current song exists
        if self.current_song is not None:
            song = self.current_song.song
            print(f"Currently Playing: {song}")
        # if self.current_song is None
        else:
            print(f"At the end of the '{self.name}' playlist")

    def go_back(self):
        if self.current_song is None:
            print('Cannot go back. At the beginning of the playlist')
        else:
            self.current_song = self.current_song.prev
            if self.current_song is not None:
                song = self.current_song.song
                print(f"Currently Playing: {song}")
            # if self.current_song is None
            else:
                print(f"At the beginning of the '{self.name}' playlist")


print('='*150)

workout_warriors = PlaylistManager("Workout Warriors")

# Add songs to the playlist
workout_warriors.add_song("Start Me Up", "The Rolling Stones", "3:33", "Rock")
workout_warriors.add_song("Thunderstruck", "AC/DC", "4:52", "Rock")
workout_warriors.add_song("Crank That (Soulja Boy)", "Soulja Boy", "3:41", "Hip-Hop")
workout_warriors.add_song("Seven Nation Army", "The White Stripes", "3:59", "Rock")


workout_warriors.play_next()
workout_warriors.play_next()
workout_warriors.play_next()

workout_warriors.go_back()
workout_warriors.go_back()
workout_warriors.go_back()

# In Class Exercise:
print("""
You are tasked with building an inventory management system for a bookstore. The system 
should allow adding new books to the inventory and removing books based on their ISBN. You'll 
implement this system using a linked list data structure.

**Instructions:**

1. Create a class named **`Book`** with attributes for title, author, genre, ISBN, and quantity.
2. Create a class named **`Node`** to represent nodes in the linked list. Each node will store a book object.
3. Implement a class named **`InventoryManager`** to manage the inventory using a linked list.
4. Implement the following methods in the **`InventoryManager`** class:
    - **`add_book(title, author, genre, isbn, quantity)`**: Adds a new book to the inventory.
    - **`remove_book(isbn)`**: Removes a book from the inventory based on its ISBN.
    - **`display_inventory()`**: Displays the current inventory.
""")

class Book:
    def __init__(self, title, author, genre, isbn, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.quantity = quantity

    def __str__(self):
        return f"{self.title} by {self.author}\nISBN: {self.isbn}\nGenre: {self.genre}\nQuantity: {self.quantity}\n"

class Node:
    def __init__(self, book):
        self.book = book
        self.next = None

class InventoryManager:
    def __init__(self):
        self.head = None

    def add_book(self, title, author, genre, isbn, quantity):
        new_book = Book(title, author, genre, isbn, quantity)
        new_node = Node(new_book)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node

    def remove_book(self, isbn):
        if not self.head:
            print('Empty Inventory')
            return
        if self.head.book.isbn == isbn:
            self.head = self.head.next
        else:
            node = self.head
            while node.next:
                if node.next.book.isbn == isbn:
                    print(f"{node.next.book.title} has been removed")
                    node.next = node.next.next
                    return
                node = node.next
            print(f"{isbn} is not in the Inventory")

    def display_inventory(self):
        node = self.head
        while node:
            print(node.book)
            node = node.next

inventory = InventoryManager()

inventory.add_book('The Outsiders', 'S.E. Hinton', 'Young Adult', '123456789', 101)
inventory.add_book('Green Eggs and Ham', 'Dr. Seuss', 'Childrens', '987654321', 250)
inventory.add_book('Dune', 'Mr. Dune', 'Fiction', '192837465', 50)

inventory.display_inventory()

inventory.remove_book('987654321')

inventory.display_inventory()