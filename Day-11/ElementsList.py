def sum_of_list(lst):
    return sum(lst)

number = list(map(int,input("Enter a number seprated by spaces : ").split()))

print("Sum of the list is : ",sum_of_list(number))
