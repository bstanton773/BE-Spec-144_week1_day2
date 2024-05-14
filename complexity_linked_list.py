import time
from linked_lists import SinglyLinkedList


# Adding 1000 nodes to the beginning of a Linked List - .push - O(1)

linked_list_a = SinglyLinkedList()

start = time.time()

for i in range(1000):
    linked_list_a.push(i)

end = time.time()

print("Time it takes to push 1000 elements to the beginning of the LinkedList:", end - start)

# Adding 1000 nodes to the end of a Linked List - .append - O(n)

linked_list_b = SinglyLinkedList()

start = time.time()

for i in range(1000):
    linked_list_b.append(i)

end = time.time()

print("Time it takes to append 1000 elements to the end of the LinkedList:", end - start)




# The builtin Python list has the opposite complexities
normal_list_a = []

start = time.time()

for i in range(1000):
    normal_list_a.append(i)

end = time.time()

print("Time it takes to append 1000 elements to the end of the Python list:", end - start)


normal_list_b = []

start = time.time()

for i in range(1000):
    normal_list_a.insert(0,i)

end = time.time()

print("Time it takes to insert 1000 elements to the beginning of the Python list:", end - start)
