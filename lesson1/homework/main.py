# Problem 1
# Ask the user for a word.
# Print the word reversed using slicing.
print("Problem 1")
word = input("Enter a word:")
print(word[::-1])

# Problem 2
# Ask the user for a word and a letter.
# Print how many times the letter appears in the word (case-insensitive)
print("Problem 2")  
word = input("Enter a word:")

while True:
  letter = input("Enter a letter:")
  if letter == "" or len(letter) > 1:                                                   
      print("this is not a valid letter, please enter a single letter.")
  elif not letter.isalpha():
        print("Invalid input. Please enter a letter (A-Z), not a number or symbol.")
  else:
      break
#if not letter:  
#    print("You didnt enter a letter,")
#    letter = input("Enter a letter again:")
count = word.lower().count(letter.lower())
print(f"The letter '{letter}' appears {count} times in the word '{word}'.") 

# Problem 3
# Ask the user for an email address like "name@example.com".
# Print only the part after the @ (example: "example.com")  
print("Problem 3")
while True:
    email = input("Enter an email address: ")
    if '@' not in email:
        print("Invalid email address. Please include an '@' symbol.")  
    elif email.count('@') > 1:
        print("Invalid email address. Please include only one '@' symbol.")
    elif email.startswith('@') or email.endswith('@'):
        print("Invalid email address. The '@' symbol cannot be at the start or end.")
    else: 
        break

domain = email.split('@')[1]
print(f"The domain of the email address is: {domain}")

# Problem 4
# Ask the user for a word.
# Print the word without the first and last character.
print("Problem 4")
word = input("Enter a word: ")
print(word[1:-1])

# Problem 5
# Ask the user for a sentence.
# Print "Long" if the sentence has more than 20 characters (including spaces),
# otherwise print "Short".
print("Problem 5")
sentence = input("Enter a sentence: ")
if len(sentence) > 20:
    print("Long")
else:
    print("Short")
