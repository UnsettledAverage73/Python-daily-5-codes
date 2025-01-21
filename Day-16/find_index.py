def find_index(array, element):
	try:
		index = array.index(element)
	except ValueError:
		index = -1
	return index
	
array = [10, 20, 30, 40, 50] 
element = 30 
result = find_index(array, element)
print("Index of",element,":",result)
