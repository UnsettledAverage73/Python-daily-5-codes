def factorial(n):
    if n == 0 or n == 1 :
        return 1
    else :
        return n * factorial(n-1)

#taking input
num = int(input("Enter a number to calculate its factorial : "))

#calling the recursive fuction and outpuuting the result

result=factorial(num)

print(f"The factorial of {num} is : {result}")
