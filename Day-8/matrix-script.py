def merge_the_tools(string, k):
    # Iterate through the string in steps of size 'k'
    for i in range(0, len(string), k):
        # Extract the substring of size k
        substring = string[i:i+k]
        # Create an empty string to store the result
        result = ''
        # Iterate through the substring
        for char in substring:
            # Add the character to result if it is not already present
            if char not in result:
                result += char
        # Print the processed substring
        print(result)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
