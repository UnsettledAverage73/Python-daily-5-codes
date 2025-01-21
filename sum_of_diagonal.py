def sum_of_diagonal(array):
	diagonal_sum = sum(array[i][i] for i in range(len(array)))
	return diagonal_sum


# Input
array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = sum_of_diagonal(array)
print("Sum of diagonal elements:",result)

