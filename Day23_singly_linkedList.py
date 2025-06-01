"""
Day 23: Singly Linked List - Basics, Traversal, and Insertion at End

📚 Concept:
A singly linked list is a linear data structure where each element (node)
points to the next one using a reference. It enables dynamic memory allocation
and is useful when you expect frequent insertions/deletions.

🧠 Real-world Analogy:
Think of a treasure hunt, where each clue leads you to the next clue.
You can't skip directly to the 4th clue without first reading the 1st, 2nd, and 3rd.

✅ Topics Covered:
- Node class
- LinkedList class
- Traversal
- Insertion at end
"""

# Step 1: Define the Node class
class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node

# Step 2: Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Start of the linked list

    # Traverse and print the linked list
    def traverse(self):
        current = self.head
        print("🔗 Linked List Traversal:")
        while current:
            print(f"[{current.data}] → ", end="")
            current = current.next
        print("None")

    # Insert a new node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"✅ Inserted {data} as the head node.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"✅ Inserted {data} at the end of the list.")

# Step 3: Create and use the linked list
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.traverse()

"""
🧪 Sample Output:

✅ Inserted 10 as the head node.
✅ Inserted 20 at the end of the list.
✅ Inserted 30 at the end of the list.
🔗 Linked List Traversal:
[10] → [20] → [30] → None
"""

