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