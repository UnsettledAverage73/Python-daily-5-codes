matrix=[
    [1,2,3],
    [2,3,4],
    [3,4,5]
]

transpose=[[row[i] for row in matrix] for i in range(len(matrix[0]))]

print("Original matrix")
for row in matrix :
    print(row)

print("\nTransposed Matrix:")
for row in transpose:
    print(row)

if (matrix==transpose):
    print("Ohh damn")
else :
    print("no")
