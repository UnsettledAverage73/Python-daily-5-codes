"""
Day 24: Singly Linked List - Insertion at Beginning and Specific Position

🧠 Why?
Singly Linked Lists allow flexible memory management and insertions at any position.
Compared to arrays, inserting at the beginning or middle doesn't require shifting all elements.

✅ Covered:
- Insert at beginning
- Insert at specific index (0-based)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        current = self.head
        print("🔗 Linked List Traversal:")
        while current:
            print(f"[{current.data}] → ", end="")
            current = current.next
        print("None")

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Point new node to current head
        self.head = new_node       # Make new node the head
        print(f"✅ Inserted {data} at the beginning.")

    def insert_at_position(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        pos = 0

        while current is not None and pos < index - 1:
            current = current.next
            pos += 1

        if current is None:
            print("❌ Index out of bounds.")
            return

        new_node.next = current.next
        current.next = new_node
        print(f"✅ Inserted {data} at position {index}.")

# Test the code
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)

    ll.insert_at_beginning(5)     # Should be the new head
    ll.insert_at_position(2, 15)  # Insert between 10 and 20

    ll.traverse()

"""
🧪 Sample Output:
✅ Inserted 5 at the beginning.
✅ Inserted 15 at position 2.
🔗 Linked List Traversal:
[5] → [10] → [15] → [20] → [30] → None
"""

