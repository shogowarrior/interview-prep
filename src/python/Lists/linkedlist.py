import random

class Node:
    def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")

        dummy = Node(0)        # 👈 Create dummy node
        dummy.next = self.head # Dummy points to current head
        curr = dummy

        for _ in range(index):
            curr = curr.next

        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node

        self.head = dummy.next # 👈 Update head (in case we inserted at index 0)
        self.size += 1
        del dummy

    # Add a new node at the end
    def append(self, data):
        # Create a new node and assign data to it
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def generate_random(self, length, min_val=0, max_val=100):
        """Generate a linked list with random numbers"""
        for _ in range(length):
            self.append(random.randint(min_val, max_val))

            
    # Print the linked list
    def display(self):
        print("Linked List size: ", self.size)
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Search for a value
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # Delete a node by value
    def delete(self, key):
        # Create a dummy node to delete the head node if it matches the key
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        curr = self.head
        while curr:
            if curr.data == key:
                prev.next = curr.next
                self.head = dummy.next
                return
            prev, curr = curr, curr.next
        del dummy

    def create_cycle(self, pos):
        if pos < 0:
            return
        curr = self.head
        cycle_node = None
        idx = 0
        while curr:
            if idx == pos:
                cycle_node = curr
            if not curr.next:
                curr.next = cycle_node
                return
            curr = curr.next
            idx += 1