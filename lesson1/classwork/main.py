word = "pineapple"
# 'p' is at index 0.
# 'i' is at index 1.

# Strings are 0 indexed (first character is index 0)
print("First letter:", word[0])
print("Second letter:", word[1])
print("Third letter:", word[2])

# Negative indexing starts from the end
print("Last letter:", word[-1])
print("Second to last letter:", word[-2])

# Slicing: word[start:stop] (start is inclusive, stop is exclusive) [start, stop)
print(word[0:4])
print(word[4:9])

# Shortcuts: you can leave the start or stop blank
print(word[:4])
print(word[4:])

# Step: word[start:stop:step]
print(word[::2])  # every other character
print(word[::-1]) # reverse string

# Error: index out of range
# print(word[100])