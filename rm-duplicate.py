def remove_duplicates(input_string):
	# create an empty set
	seen = set()
	
	#char for char in input_string : iterates each character in input string
	#if not(char in seen or seen.add(char)) : 
	# 	char in seen: check if exist in seen set
	#	add() function return None,  evalutes false in context
	# 	or : combines both conditions
	result = ''.join([char for char in input_string if not (char in seen or seen.add(char))])
	return result

input_string = "programming"
print(f"Input: {input_string}")

#after remove duplication
string = remove_duplicates(input_string)
print(f"Output: {string}")
