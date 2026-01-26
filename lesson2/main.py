# Problem 1
# Ask the user for a sentence.
# Print how many words it has.
# (Hint: split the sentence by spaces)
print("Problem 1")
while True:
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    if sentence==""  or len(words) < 2:
        print("This is not a valid sentence")
        
    else:
      break    
print("Number of words:", len(words)) 

# Problem 2
# Ask the user for a word.
# Build a new string that turns every vowel into "*".
# Example: "hello" -> "h*ll*"
print("\nProblem 2")
word = input("Enter a word: ")
vowels = "aeiouAEIOU"   
new_word = ""                                                                                                       
for char in word:
    if char in vowels:
        new_word += "*"
    else:
        new_word += char
print("Transformed word:", new_word)

# Problem 3
# Ask the user for a word.
# Print the first index where the letter "a" appears.
# If there is no "a", print -1.
print("\nProblem 3")
word = input("Enter a word: ")
index = word.find("a")  
if index == -1:
    print("-1")
else:                       
   print("Index of first 'a':", index)

 # Problem 4
# Ask the user for two words.
# Print the longer word. If they are the same length, print "Tie".
print("\nProblem 4")
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
if len(word1) > len(word2):             
    print("Longer word:", word1)
elif len(word2) > len(word1):
    print("Longer word:", word2)
else:
    print("Tie")




# Problem 5
# Ask the user for a phrase.
# Build a new string that keeps only letters (remove spaces and punctuation).
# For this problem, remove commas and periods too.
print("\nProblem 5")            
phrase = input("Enter a phrase: ")          
new_phrase = ""
for char in phrase:     
    if char.isalpha():  
        new_phrase += char
print("Filtered phrase:", new_phrase)   
