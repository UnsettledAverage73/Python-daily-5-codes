def reverse_string(input_string):
	#using slicing
	reverse_string = input_string[::-1]
	return reverse_string

#Input
input_string = "hello"

output_string = reverse_string(input_string)

print("Input:",input_string)
print("Output:",output_string)
