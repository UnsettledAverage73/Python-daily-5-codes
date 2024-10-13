def is_prime(number):
    if number < 2 :
        return False
    for i in range(2,int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

num = int(input("Enter a number : "))

output = is_prime(num)

if output:
    print(f"It is {num} is Prime number")
else :
    print(f"It is {num} is not a Prime number")
