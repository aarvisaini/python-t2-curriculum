# Problem 1
# Create a class called BankAccount.
# __init__ takes owner and balance.
# Make a method deposit(amount) that adds to balance.
# Make a method withdraw(amount) that subtracts only if there is enough money.
# Test it with a few deposits and withdrawals.
print("Problem 1:") 
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

account = BankAccount("Alice", 100)
account.deposit(50)
print(account.balance)  
account.withdraw(30)
print(account.balance)  
account.withdraw(200)  

# Problem 2
# Create a class called Car.
# __init__ takes model and miles.
# Make a method drive(distance) that adds to miles.
# Create a Car and drive it a few times, printing miles each time.
print("\nProblem 2:")
class Car:          
    def __init__(self, model, miles):
        self.model = model
        self.miles = miles

    def drive(self, distance):
        self.miles += distance  
car = Car("Toyota", 10000)                                      
car.drive(150)
print(car.miles)  # Should be 10150
car.drive(200)
print(car.miles)  # Should be 10350


# Problem 3
# Create a class called ScoreKeeper.
# It stores a dictionary of player scores.
# Make a method add_points(name, points) that adds points for that player.
# Print the final dictionary after adding points for a few players.
print("\nProblem 3:")
class ScoreKeeper:
    def __init__(self):
        self.scores = {}

    def add_points(self, name, points):
        if name in self.scores:
            self.scores[name] += points
        else:
            self.scores[name] = points
score_keeper = ScoreKeeper()
score_keeper.add_points("Alice", 10)
score_keeper.add_points("Bob", 15)
score_keeper.add_points("Alice", 5)
print(score_keeper.scores)  # Should be {'Alice': 15, 'Bob': 15}
    

# Problem 4
# Create a class called Timer.
# It starts at 0 seconds.
# Make a method tick() that adds 1.
# Make a method reset() that sets it back to 0.
# Test tick() and reset().
print("\nProblem 4:")
class Timer:                                
    def __init__(self):
        self.seconds = 0

    def tick(self):
        self.seconds += 1

    def reset(self):
        self.seconds = 0    
timer = Timer()
timer.tick()
timer.tick()
print(timer.seconds)  # Should be 2
timer.reset()
print(timer.seconds)  # Should be 0

# Problem 5
# Create a class called WordTracker.
# It stores a word (string).
# Make a method add_letter(letter) that adds the letter to the end.
# Make a method remove_last() that removes the last letter (if it exists).
# Test it.
print("\nProblem 5:")
class WordTracker:
    def __init__(self, word):
        self.word = word

    def add_letter(self, letter):
        self.word += letter

    def remove_last(self):
        if len(self.word) > 0:
            self.word = self.word[:-1]

tracker = WordTracker("hello")
tracker.add_letter("!")
print(tracker.word)  # Should be "hello!"
tracker.remove_last()
print(tracker.word)  # Should be "hello"