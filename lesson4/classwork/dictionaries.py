# A dictionary maps keys to values
person = {
    "name": "Alex",
    "age": 15,
    "city": "Seattle"
}
# dictionaries cannot have the same key twice, but they can have the same value
print(person)

# print a value at a key
print("Name:", person["name"])
print("Age:", person["age"])

# add a new key to your dictionary
person["favorite_food"] = "pizza"
print(person)

# modify an existing key in your dictionary
person["age"] = 16
print("New age: " + str(person["age"]))

person["age"] = person["age"] + 1
print("New age: ", person["age"])

# checks if a key is in our dictionary
print("age" in person)
if "height" in person:
    print("I know this person's height.")