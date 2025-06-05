"""
Day 27: Queue using Linked List

🧠 Why?
A queue lets you model real-world waiting lines (tasks, processes, services) with dynamic memory using linked lists.

✅ Covered:
- enqueue(data): Add to rear
- dequeue(): Remove from front
- peek(): View front
- is_empty(): Check if queue is empty
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            print(f"✅ Enqueued {data} (first element).")
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"✅ Enqueued {data} to queue.")

    def dequeue(self):
        if self.is_empty():
            print("❌ Queue Underflow – nothing to dequeue.")
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:  # Queue becomes empty
            self.rear = None
        print(f"🗑️ Dequeued {removed_data} from queue.")
        return removed_data

    def peek(self):
        if self.is_empty():
            print("🔍 Queue is empty.")
            return None
        print(f"👀 Front of queue: {self.front.data}")
        return self.front.data

    def display(self):
        print("🧱 Queue (Front → Rear):")
        current = self.front
        while current:
            print(f"[{current.data}]", end=" → ")
            current = current.next
        print("None")


# Test the queue
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    q.display()

    q.peek()
    q.dequeue()
    q.display()
