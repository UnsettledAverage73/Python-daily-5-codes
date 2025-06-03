"""
Day 25: Singly Linked List – Deletion from Beginning, End, and Specific Position

🧠 Why?
Understanding how to remove nodes from a linked list is key to mastering memory management and dynamic data structures.

✅ Covered:
- delete_from_beginning()
- delete_from_end()
- delete_from_position(index)
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

    def delete_from_beginning(self):
        if self.head is None:
            print("❌ List is empty. Nothing to delete.")
            return
        print(f"🗑️ Deleted {self.head.data} from beginning.")
        self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            print("❌ List is empty. Nothing to delete.")
            return
        if self.head.next is None:
            print(f"🗑️ Deleted {self.head.data} (only node in list).")
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next
        print(f"🗑️ Deleted {current.next.data} from end.")
        current.next = None

    def delete_from_position(self, index):
        if index == 0:
            self.delete_from_beginning()
            return
        current = self.head
        pos = 0

        while current is not None and pos < index - 1:
            current = current.next
            pos += 1

        if current is None or current.next is None:
            print("❌ Index out of bounds.")
            return

        print(f"🗑️ Deleted {current.next.data} from position {index}.")
        current.next = current.next.next


# Test the code
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    ll.insert_at_end(50)

    ll.traverse()

    ll.delete_from_beginning()   # 10 removed
    ll.delete_from_end()         # 50 removed
    ll.delete_from_position(1)   # 30 removed (index 1 after 10 deleted)

    ll.traverse()

"""
🧪 Output:
🔗 Linked List Traversal:
[10] → [20] → [30] → [40] → [50] → None
🗑️ Deleted 10 from beginning.
🗑️ Deleted 50 from end.
🗑️ Deleted 30 from position 1.
🔗 Linked List Traversal:
[20] → [40] → None
"""

