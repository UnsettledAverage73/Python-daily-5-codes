num1 = float(input("Enter a number1 : "))
num2 = float(input("Enter a number2 :"))
num3 = float(input("Enter a number3 : "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2>=num1) and (num2>=num3):
    largest=num2
else:
    largest=num3

print(f"The largest Number is {largest}")