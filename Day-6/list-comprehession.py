# Input reading
x = int(input())
y = int(input())
z = int(input())
n = int(input())

# List comprehension to generate all possible coordinates where x + y + z is not equal to n
# Syntax of list comprehesnion 
# [expression for item1 in iterable1 for item2 in iterable2 ... if condition]

coordinates = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

# Print the result
print(coordinates)
