# Problem 1
# Create a class called Cat.
# It should have an __init__ that takes name.
# It should have a method called meow() that prints "<name> says meow!".
# Create a Cat and call meow(). 
class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} says meow!")    
my_cat = Cat("Whiskers")
my_cat.meow()

# Problem 2
# Create a class called Rectangle.
# __init__ should take width and height.
# Make a method area() that returns width * height.
# Create a Rectangle and print its area.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
my_rectangle = Rectangle(5, 3)
print(my_rectangle.area())

# Problem 3
# Create a class called Counter.
# It starts at value 0.
# Make a method add_one() that increases the value by 1.
# Call add_one() 5 times and print the final value.
class Counter:
    def __init__(self):
        self.value = 0

    def add_one(self):
        self.value += 1
my_counter = Counter()
for _ in range(5):
    my_counter.add_one()
print(my_counter.value)

# Problem 4
# Create a class called Player.
# __init__ takes name and health.
# Make a method take_damage(amount) that subtracts from health (no negatives).
# Create a Player and test take_damage().
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
my_player = Player("Hero", 100)
my_player.take_damage(30)
print(my_player.health)
my_player.take_damage(80)
print(my_player.health) 


# Problem 5
# Create a class called Book.
# __init__ takes title and pages.
# Make a method is_long() that prints "Long" if pages >= 300, else prints "Short".
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def is_long(self):
        if self.pages >= 300:
            print("Long")
        else:
            print("Short")                             
my_book = Book("War and Peace", 1225)
my_book.is_long()
my_short_book = Book("Short Story", 150)
my_short_book.is_long() 