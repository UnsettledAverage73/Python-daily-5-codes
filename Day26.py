"""
Day 26: Stack using Linked List

🧠 Why?
Unlike array-based stacks, linked list stacks are not limited by fixed size. They grow as needed.

✅ Covered:
- push(item): Insert item at the top (beginning)
- pop(): Remove item from the top
- peek(): View top item
- is_empty(): Check if stack is empty
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None  # Points to the top node

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top  # New node points to old top
        self.top = new_node       # New node becomes the new top
        print(f"✅ Pushed {data} onto stack.")

    def pop(self):
        if self.is_empty():
            print("❌ Stack Underflow – nothing to pop.")
            return None
        popped = self.top.data
        self.top = self.top.next  # Remove top
        print(f"🗑️ Popped {popped} from stack.")
        return popped

    def peek(self):
        if self.is_empty():
            print("🔍 Stack is empty.")
            return None
        print(f"👀 Top of stack is: {self.top.data}")
        return self.top.data

    def display(self):
        print("🧱 Stack (Top to Bottom):")
        current = self.top
        while current:
            print(f"[{current.data}]")
            current = current.next
        print("-" * 20)


# Test the stack
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    stack.display()

    stack.peek()
    stack.pop()
    stack.pop()

    stack.display()

