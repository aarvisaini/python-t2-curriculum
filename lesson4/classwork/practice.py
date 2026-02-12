# Problem 1
# Create a dictionary called student with these keys:
# "name" -> your name
# "grade" -> your grade level
# Print the dictionary and then print only the name.
student = {
    "name": "Aarvi",
    "grade": 4
} 
print(student)
print(student["name"])                  

# Problem 2
# Create a dictionary called prices with:
# "apple" -> 2
# "banana" -> 1
# "orange" -> 3
# Ask the user for a fruit name and print its price.
# If the fruit is not in the dictionary, print "Not found".
prices = {
    "apple": 2,
    "banana": 1,
    "orange": 3
}
fruit = input("Enter a fruit name: ")               
if fruit in prices:
    print("The price of", fruit, "is", prices[fruit])
else:    print("Not found")


# Problem 3
# Ask the user for a word.
# Use a dictionary to count how many times each letter appears.
# Print the dictionary.
word = input("Enter a word: ")      
freq = {}
for character in word:
    if character in freq:
        freq[character] = freq[character] + 1
    else:
        freq[character] = 1

print(freq)


# Problem 4
# Create a dictionary called phonebook with names and phone numbers.
# Ask the user for a name and print the phone number if it exists.
# Otherwise print "Unknown contact".
phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}
name = input("Enter a name: ")
if name in phonebook:
    print("The phone number of", name, "is", phonebook[name])
else:    print("Unknown contact")   


# Problem 5
# Create a dictionary called scores with 3 students and their test scores.
# Print the name of the student with the highest score.
scores = {
    "Ava": 95,
    "Ben": 88,
    "Kai": 73,
}
highest_score = 0
top_student = ""
for name, score in scores.items():
    if score > highest_score:
        highest_score = score
        top_student = name          