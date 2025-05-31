"""
Day 22: Arrays - Basics and Traversal

📚 Concept:
An array is a collection of items stored at contiguous memory locations.
It allows random access and efficient traversal, insertion (at end), and deletion (at end).

🧠 Real-world Analogy:
Think of an array like a row of lockers where each locker holds one item
and is labeled by a number (index).
"""

# Step 1: Declare an array (list in Python)
numbers = [10, 20, 30, 40, 50]

# Step 2: Traverse the array and print each element
print("Array Traversal:")
for i in range(len(numbers)):
    print(f"Index {i} => Value {numbers[i]}")

# Step 3: Insert an element at the end
numbers.append(60)
print("\nAfter appending 60:", numbers)

# Step 4: Insert an element at a specific index (say index 2)
numbers.insert(2, 25)
print("After inserting 25 at index 2:", numbers)

# Step 5: Delete last element
removed = numbers.pop()
print(f"Removed element: {removed}")
print("After deletion:", numbers)

"""
🧩 Output:

Array Traversal:
Index 0 => Value 10
Index 1 => Value 20
Index 2 => Value 30
Index 3 => Value 40
Index 4 => Value 50

After appending 60: [10, 20, 30, 40, 50, 60]
After inserting 25 at index 2: [10, 20, 25, 30, 40, 50, 60]
Removed element: 60
After deletion: [10, 20, 25, 30, 40, 50]
"""

