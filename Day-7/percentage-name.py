if __name__ == '__main__':
    # Read number of students
    n = int(input())

    # Create an immutable dictionary to store the students and their marks
    students_marks = {}

    # Input each student's name and their marks
    for _ in range(n):
        data = input().split()  # Split input into a list
        name = data[0]  # First element is the student's name
        marks = list(map(float, data[1:]))  # The rest are the marks
        students_marks[name] = marks  # Store in the dictionary

    # Input the query name
    query_name = input()

    # Retrieve the marks for the query_name
    query_marks = students_marks[query_name]

    # Calculate the average of the marks
    average = sum(query_marks) / len(query_marks)

    # Print the average, formatted to 2 decimal places
    print(f"{average:.2f}")
