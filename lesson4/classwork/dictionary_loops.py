scores = {
    "Ava": 95,
    "Ben": 88,
    "Kai": 73,
}

# Loop through only keys
for name in scores:
    print(name, "scored", scores[name])

# get a list of dictionary keys
print(list(scores.keys()))

# get a list of dictionary values
print(list(scores.values()))

# get a list of both dictionary keys and values
print(list(scores.items()))

# loop through keys and values
for name, score in scores.items():
    if score >= 90:
        print(name, "got an A.")

# loop through only values.
for value in scores.values():
    print(value)

# loop through only keys
for key in scores.keys():
    print(key)