# Fuction to calculate sum of elements in a list using recursion

''' concept : eg . numbers = 2 4
                then it calls function 
    recursively answer :
            it calculates len which is equal to 2 
           first call
            sum_of_list([2 , 4])
                lst[0] = 2
            second call
                sum_of_list([4])
                lst[0] = 4 
            recursively call sum_of_list([]) list is empty so return 0.
        `   
            the total sum is [2 , 4 ] is 6

            first element + the sum of the rest of the list;;
'''



def sum_of_list(lst):
    if len(lst) == 0 :
        return 0
    else :
        return lst[0] + sum_of_list(lst[1:])

numbers = list(map(int , input("Enter number separated by spaces : ").split()))
print(f"Sum of the list is : ",sum_of_list(numbers))
