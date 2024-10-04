if __name__ == '__main__':
    # Read the number of students
    n = int(input())
    
    # Initializing a nested list to store names and scores
    students = []

    # Loop to read each student's name and score
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])  # Append as a nested list

    # Extracting grades and finding unique ones
    grades = sorted(set(student[1] for student in students))

    # Check if there is a second lowest grade
    if len(grades) < 2:
        print("There is no second lowest grade.")
    else:
        second_lowest_grade = grades[1]

        # Finding all names with the second lowest grade
        second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

        # Sorting names alphabetically
        second_lowest_students.sort()

        # Printing each name on a new line
        for name in second_lowest_students:
            print(name)
