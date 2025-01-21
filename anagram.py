#Anagram: in python soreted
#	Two string are anagram if:
# 1.They contain the same characters.
# 2.Each character appears the same number of times in both strings.
# 3.Order of characters does not matter.
# 4.The comparison should ignore case and spaces.

#Ex. "listen" and "silent" are anagrams.
#    "hello" and "world" are not angrams.

def are_anagram(string1, string2)
	
	#remove space and convert into lowercase
	string1 = string1.replace(" ","").lower()
	string2 = string2.replace(" ","").lower()

	#check if sorted character are equal
	return sorted(string1) == sorted(string2)

string1 = "listen"
string2 = "silent"

if are_anagram(string1,string2):
	print("Yes it is anagram")
else :
	print("Not it is not anagram")


