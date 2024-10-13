# Fuction to calculate nth fibonacci number using recursion

# Cocepts :

#1) if value of n is 1 or less than 1 then print that number eg. n = 1 then print 1 .
#2) and if value greater than 1 means suppose value is 3 then ( 7fibonacci of 2 + fibonacci of 1 ) 

# Fibonnaci series 0 1 1 2 3 5 8 13 21 34 55 89 ................
def fibonacci(n):
    if  n <= 1:
        return n
    else :
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci_sequence(n):
    for i in range(n):
        print(fibonacci(i) , end=" ")

terms = int(input("Enter the number of terms : "))

print_fibonacci_sequence(terms)
