def minion_game(string):

    # Length of the string
    n = len(string)
    
    # Initialize scores for both players
    kevin_score = 0
    stuart_score = 0
    
    # Loop through each character in the string
    for i in range(n):
        # Check if the character is a vowel
        if string[i] in 'AEIOU':
            # Kevin's score is increased by (n - i) substrings starting from this vowel
            kevin_score += n - i
        else:
            # Stuart's score is increased by (n - i) substrings starting from this consonant
            stuart_score += n - i
    
    # Determine and print the winner
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
