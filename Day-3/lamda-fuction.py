# Lambda function to calculate the square of a number

# Defining the lambda function
square = lambda x: x ** 2
avg = lambda x , y , z : (x + y + z)/3

# Taking input from the user
num = int(input("Enter a number to calculate its square: "))

# Calling the lambda function
result = square(num)

cube_result = avg(2,3,5)

# Outputting the result
print(f"The square of {num} is: {result}")
print(f"The average of is {cube_result}")

