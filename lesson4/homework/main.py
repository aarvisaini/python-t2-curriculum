# Problem 1
# Ask the user for a sentence.
# Use a dictionary to count how many times each word appears.
# Print the dictionary.
# (Hint: split the sentence)
print("problem 1")
sentence = input("Enter a sentence: ")
word_count ={}

for word in sentence.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1    
print(word_count)
print("There are " + str(len(word_count)) + " unique words in the sentence")


# Problem 2
# Create a dictionary called capitals with states and their capitals.
# Ask the user for a state and print the capital.
# If not found, print "No data".
print("\nproblem 2")
capitals = {
    "California": "Sacramento",
    "Texas": "Austin",
    "Florida": "Tallahassee",
    "New York": "Albany",
    "Illinois": "Springfield",
    "Pennsylvania": "Harrisburg",
    "Ohio": "Columbus",
    "Georgia": "Atlanta",
    "North Carolina": "Raleigh",
    "Michigan": "Lansing",
    "Washington": "Olympia",
    "Arizona": "Phoenix",
    "Massachusetts": "Boston",
    "Tennessee": "Nashville",
    "Indiana": "Indianapolis",
    "Missouri": "Jefferson City",
    "Maryland": "Annapolis",
    "Wisconsin": "Madison",
    "Colorado": "Denver",
    "Minnesota": "St. Paul",
    "South Carolina": "Columbia",
    "Alabama": "Montgomery",
    "Louisiana": "Baton Rouge",
    "Kentucky": "Frankfort",
    "Oregon": "Salem",
    "Oklahoma": "Oklahoma City",
    "Connecticut": "Hartford",      
    "Iowa": "Des Moines",
    "Utah": "Salt Lake City",
    "Nevada": "Carson City",
    "Arkansas": "Little Rock",
    "Mississippi": "Jackson",
    "Kansas": "Topeka",
    "New Mexico": "Santa Fe",
    "Nebraska": "Lincoln",
    "West Virginia": "Charleston",
    "Idaho": "Boise",
    "Hawaii": "Honolulu",
    "New Hampshire": "Concord",
    "Maine": "Augusta",
    "Rhode Island": "Providence",
    "Montana": "Helena",        
    "Delaware": "Dover",    
    "South Dakota": "Pierre",
    "North Dakota": "Bismarck",
    "Alaska": "Juneau",
    "Vermont": "Montpelier",
    "Wyoming": "Cheyenne",
    "District of Columbia": "Washington D.C.",
    "Puerto Rico": "San Juan",
    "Guam": "Hagåtña",
}
lowercase_capitals = {state.lower(): capital for state, capital in capitals.items()}
state = input("Enter a state: ")
if state.lower() in lowercase_capitals:
    print(lowercase_capitals[state.lower()])
else:
    print("No data")

# Problem 3
# Ask the user for a word.
# Print the letter that appears the most times.
# If there is a tie, print any one of them.
print("\nproblem 3")
word = input("Enter a word: ")          
letter_count = {}
for letter in word: 
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
most_common_letter = max(letter_count, key=letter_count.get)
print("The most common letter is: " + most_common_letter)   


# Problem 4
# Create a dictionary called inventory with items and their quantity.
# Ask the user what item they want to buy and how many.
# If there are enough, subtract from the inventory and print the new inventory.
# Otherwise print "Not enough".
print("\nproblem 4")                                            
inventory = {
    "apple": 10,
    "banana": 20,
    "orange": 15,
    "grape": 5,
    "watermelon": 2
}
item = input("What item do you want to buy? ")
quantity = int(input("How many do you want to buy? "))
if item in inventory:
    if inventory[item] >= quantity:
        inventory[item] -= quantity
        print("New inventory: " + str(inventory))
    else:
        print("Not enough")
else:    print("Item not found")    



# Problem 5
# Ask the user for two words.
# Use dictionaries to check if they are anagrams (same letters, different order).
# Print "Anagram" or "Not anagram".
print("\nproblem 5")
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
def count_letters(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count
if count_letters(word1) == count_letters(word2):
    print("Anagram")
else:    print("Not anagram")