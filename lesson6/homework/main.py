# Problem 1
# Create a tuple called scores with 4 numbers.
# Print the average score.  
print("Problem 1")
scores = (60,80,99,100)
a,b,c,d = scores
average_score = sum(scores) / len(scores)
print("Average score:", average_score)

# Problem 2
# Create a list of tuples representing students:
# ("Ava", 95), ("Ben", 88), ("Kai", 73)
# Print the name of the student with the highest score.
print("\nProblem 2")
students = [("Ava", 95), ("Ben", 88), ("Kai", 73)]       
a,b,c = students
higest_score = max(students,key=lambda x: x[1])
print("The student with the highest score is:", higest_score[0])
# Problem 3
# Ask the user for a sentence.
# Split it into words.
# Create a list of tuples where each tuple is (word, length_of_word).
# Print the list.
print("\nProblem 3")
sentence = input("Enter a sentence: ")
words = sentence.split()
word_length_tuples = [(word, len(word)) for word in words]  
print(word_length_tuples)

# Problem 4
# Create a function called first_and_last(word).
# It should return a tuple containing the first and last letter of the word.
# Test it.
print("\nProblem 4")
def first_and_last(word):
    if len(word) == 0:
        return None
    return (word[0], word[-1])
test_word = "hello"
result = first_and_last(test_word)
print(f"The first and last letters of '{test_word}' are: {result}")

# Problem 5
# Tuples can be dictionary keys.
# Create a dictionary where the keys are points like (x, y) and the values are colors.
# Add at least 3 points and print the dictionary.
print("\nProblem 5")
point_colors = {(0, 0): "red",
    (1, 1): "blue",
    (2, 2): "green"}
print(point_colors)