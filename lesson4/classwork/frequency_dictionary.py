# count how many times each letter appears in a word
word = "balloon"

freq = {}
for character in word:
    if character in freq:
        freq[character] = freq[character] + 1
    else:
        freq[character] = 1

print(freq)