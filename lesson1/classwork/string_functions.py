text = "  Hello world  "
print("Raw text:", text)

print("Length:", len(text))  # print text length, includes spaces

print(text.lower())  # make everything lowercase
print(text.upper())  # make everything uppercase
print(text.title())  # title case

print(text.strip())  # remove spaces on the left and right of string
print(text.rstrip()) # remove spaces from just the right of a string
print(text.lstrip()) # remove spaces from just the left of a string

# you can combine multiple string functions at once:
print(text.strip().lower())

message = "banana bread"
print(message.count("na"))
print(message.find("bread"))  # index of first match (or -1)

print(message.replace("banana", "pumpkin"))  # text.replace(a, b) replaces all a in text with b.

print(message.startswith("ba"))
if message.endswith("bread"):
    print("Message is a bread.")