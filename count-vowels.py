def count_vowels(input_string):
	vowels = {'a','e','o','i','u'}
	
	#convert string to lower case for ignore case
	input_string = input_string.lower()
	
	#count the vowels
	# 1. for char in input_string  convert 'p' 'r' 'o' 'g'.....
	# 2. if char in vowels : if given character present in input_string then count 1
	# 3. sum : addition of that character
	count = sum(1 for char in input_string if char in vowels)
	return count

input_string = "Programming"
vowel_count = count_vowels(input_string)

print(f"{input_string} contain Number of vowels {vowel_count}.")
