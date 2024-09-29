# Function to check if a number is prime

def is_prime(num):
    """This function checks if the given number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to sqrt(num)
        if num % i == 0:
            return False
    return True

# Calling the function to check if a number is prime
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
