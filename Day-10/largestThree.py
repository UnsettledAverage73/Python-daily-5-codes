def largest_of_three(a,b,c):
    if a > b and a > c:
        return a
    if b > c :
        return b
    else : 
        return c

num1 = int(input("Enter a number 1 : "))
num2 = int(input("Enter a number 2 : "))
num3 = int(input("Enter a number 3 : "))

# output 

output=largest_of_three(num1,num2,num3)

print(f"The largest number between three numbers are {num1} , {num2} and {num3} are {output} ")
