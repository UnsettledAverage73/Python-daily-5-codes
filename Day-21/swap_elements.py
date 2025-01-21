def swap_elements(array,index1,index2):
	# Swapping elements
	array[index1], array[index2] = array[index2],array[index1]
	return array

array = [10,20,30,40,50]

index1 = 1
index2 = 3 

result = swap_elements(array,index1,index2)

print("Array after swapping:",result)

