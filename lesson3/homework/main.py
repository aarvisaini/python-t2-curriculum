# Problem 1
# Ask the user for a number n.
# Print all multiples of 3 from 0 to n (including n if it is a multiple of 3).
print("Problem 1")
n = int(input("Enter a number n: "))
for i in range(0, n + 1, 3):
    print(i)


# Problem 2
# Ask the user for a number n.
# Print the square of every number from 1 to n (1*1, 2*2, ...).
print("\nProblem 2")
n = int(input("Enter a number n: "))
for i in range(1, n + 1):
    print(i * i)



# Problem 3
# Ask the user for a number n.
# Print the numbers from n down to 0 (counting down).
print("\nProblem 3")
n = int(input("Enter a number n: "))
for i in range(n, -1, -1):
    print(i)

# Problem 4
# Ask the user for a word.
# Build a new string that repeats the word 5 times with spaces in between.
# Example: "hi hi hi hi hi"
print("\nProblem 4")
word = input("Enter a word: ")
repeated_word = ' '.join([word]* 5)
print(repeated_word)

# Problem 5
# Ask the user for a number n.
# Print how many numbers from 1 to n are even.
print("\nProblem 5")
n = int(input("Enter a number n: "))
even_count = 0
for i in range (1, n + 1):
    if i % 2 == 0:
        even_count += 15
print("Total even numbers from 1 to", n, ":", even_count)