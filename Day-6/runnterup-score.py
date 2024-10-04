# Reading the number of participants (not necessary for logic, but included as per usual input format)
n = int(input())

# Reading the list of scores
scores = list(map(int, input().split()))

# Finding the maximum score (the winner's score)
max_score = max(scores)

# Removing all occurrences of the maximum score
runner_up_scores = [score for score in scores if score != max_score]

# Finding the runner-up score, which is the maximum of the remaining scores
runner_up_score = max(runner_up_scores)

# Printing the runner-up score
print(runner_up_score)
