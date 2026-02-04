# Problem 1
# Use a for loop with range to print every number from 5 to 12 (including 12).
for i in range(5, 13):
    print(i)                    


# Problem 2
# Use range with step to print all even numbers from 0 to 20 (including 20).
for i in range(0, 21, 2):
    print(i)        


# Problem 3
# Ask the user for a number n.
# Print the sum of all numbers from 1 to n (including n).
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("The sum is:", total) 


# Problem 4
# Print a countdown from 10 to 1 (10, 9, 8, ... 1).
for i in range(10, 0, -1):
    print(i)    


# Problem 5
# Ask the user for a word.
# Print each character with its index on a new line.
# Example: 0 h, 1 e, 2 l, ...
word = input("Enter a word: ")
for i in range(len(word)):
    print(i, word[i])