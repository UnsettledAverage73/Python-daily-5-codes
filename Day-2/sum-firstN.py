N = int(input("Enter a number N : "))

#initializing sum and counter
total_sum=0
counter=1

#using a while loop to calculate the sum
while counter <= N:
    total_sum += counter
    counter += 1

print(f"The sum of the first {N} natural numbers is : {total_sum}")