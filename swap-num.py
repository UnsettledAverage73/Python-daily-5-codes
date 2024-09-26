# Swapping two numbers without using a temporary variable

# Initial values of a and b
a = int(input("Enter num1 :"))
b = int(input("Enter num2 :"))

#printing the values before swapping 
print(f"Before swapping : a = {a} , b = {b}")

# swapping values using multiple assignment feature 
a , b = b , a # a takes the value of b , and b takes the value of a

#printing the vales after swapping
print(f"After swapping : a = {a}, b = {b}")
