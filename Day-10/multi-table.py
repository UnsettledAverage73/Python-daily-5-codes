def multiplication_table(number):
    for i in range(1,11):
        print(f"{number} X {i} = {number*i}")

num=int(input("Enter a number: "))

multiplication_table(num)
