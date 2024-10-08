if __name__ == '__main__':
    # Initialize an empty list
    my_list = []

    # Read the number of commands
    n = int(input())

    # Execute each command
    for _ in range(n):
        # Split the input to get the command and its arguments
        command = input().split()

        # First element is the command, rest are arguments
        cmd = command[0]
        args = command[1:]  # Arguments as strings

        # Perform the operation based on the command
        if cmd == "insert":
            # Convert args to integers and perform insertion
            my_list.insert(int(args[0]), int(args[1]))
        elif cmd == "print":
            # Print the list
            print(my_list)
        elif cmd == "remove":
            # Remove the first occurrence of the element
            my_list.remove(int(args[0]))
        elif cmd == "append":
            # Append the element to the end of the list
            my_list.append(int(args[0]))
        elif cmd == "sort":
            # Sort the list
            my_list.sort()
        elif cmd == "pop":
            # Pop the last element from the list
            my_list.pop()
        elif cmd == "reverse":
            # Reverse the list
            my_list.reverse()

