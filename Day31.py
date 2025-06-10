"""
Day 31: Implement Doubly Linked List with insert and delete operations
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    # Delete a node by value
    def delete(self, value):
        curr = self.head
        while curr:
            if curr.data == value:
                # Update pointers
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next  # deleting head

                if curr.next:
                    curr.next.prev = curr.prev

                return True  # deleted
            curr = curr.next
        return False  # not found

    # Display forward
    def display(self):
        curr = self.head
        dll = []
        while curr:
            dll.append(str(curr.data))
            curr = curr.next
        return " <=> ".join(dll)


# ✅ Demo
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_end(10)
    dll.insert_end(20)
    dll.insert_end(30)
    dll.insert_end(40)

    print("🧾 DLL after insertions:", dll.display())

    dll.delete(20)
    print("❌ DLL after deleting 20:", dll.display())

    dll.delete(10)
    print("❌ DLL after deleting head (10):", dll.display())
