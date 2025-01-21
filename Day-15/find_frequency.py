def find_frequency(array):
	from collections import Counter
	frequency = Counter(array)
	return dict(frequency)

array=[1,2,2,3,3,3,4]

result = find_frequency(array)
print("Frequency of each element:",result)
