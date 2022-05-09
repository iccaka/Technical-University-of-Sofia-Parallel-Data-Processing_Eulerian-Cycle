from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
    # Print the Linked List
    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    # Length of the list
    def length(self):
        current_node = self.head
        total = 0
        while current_node:
            current_node = current_node.next
            total += 1
        return total
    # Add a Node at the end of the list
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
    # Remove a Node from the list
    def remove(self, key):
        current_node = self.head

        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            print("Node Does Not Exist")
            return
        prev_node.next = current_node.next
        current_node = None
