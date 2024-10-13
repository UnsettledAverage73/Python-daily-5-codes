''' Function to reverse a string using recursion 
    Takes a first character and move it to the end,
    then recursivey reverse the rest of the string
    eg . atharva
        reverse_string("tharva") + "a"

        reverse_string("harva") + "t"
        .
        .
        .
        .
        .
        .
        
'''

def reverse_string(s):
    if len(s) == 0 : 
        return s
    else :
        return reverse_string(s[1:]) + s[0]

string = input("Enter a string : ")
print("Reversed string : ", reverse_string(string))

