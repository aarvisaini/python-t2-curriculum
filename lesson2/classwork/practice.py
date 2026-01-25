# Problem 1
# Ask the user for a word.
# Print how many vowels it has (a, e, i, o, u).
Word = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0
for letter in Word:
    if letter in vowels:
        count += 1
print("Number of vowels:", count)

# Problem 2
# Ask the user for a word.
# Print "Palindrome" if it reads the same backwards, otherwise print "Not palindrome".
Word = input("Enter a word: ")              
if Word == Word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")     


# Problem 3
# Ask the user for a word.
# Build a new string that contains ONLY the letters at odd indexes (1, 3, 5, ...).
Word = input("Enter a word: ")
new_string = ""                     
for i in range(1, len(Word), 2):
    new_string += Word[i]                   
print("Letters at odd indexes:", new_string)



# Problem 4
# Ask the user for two words.
# Print the two words combined with a dash in the middle. Example: "cat-dog".
Word1 = input("Enter the first word: ")             
Word2 = input("Enter the second word: ")
combined = Word1 + "-" + Word2      
print("Combined words:", combined)


# Problem 5 
# Ask the user for a phrase.
# Build a new string that removes all spaces.
Phrase = input("Enter a phrase: ")
new_phrase = ""                    
for char in Phrase:             
    if char != " ":                     
        new_phrase += char          