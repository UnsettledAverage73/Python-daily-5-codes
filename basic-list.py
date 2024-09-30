#!/bin/python

fruits=["apple","banana","cherry","mango","orange"]

print(f"First fruit : {fruits[0]}")
print(f"Last fruit : {fruits[4]}")

#Adding a new fruits to the list
fruits.append("grapes")
print(f"List after adding 'grapes' : {fruits}")

#Removing a fruit from the list
fruits.remove("banana")
print(f"List after removing 'banana' : {fruits}")

#sorting the list
fruits.sort()
print(f"Sorted List: {fruits}")

