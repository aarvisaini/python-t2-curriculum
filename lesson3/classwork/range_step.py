# range (start, stop, step)
# step controls how much the number changes each time.

print("Every number between 0 and 10, changing by 2:")
for i in range(0, 11, 2):  # [0, 11)
    print(i)

print("Every number between 10 and 1, changing by -1:")
# step can be negative (decreasing range)
for i in range(10, 0, -1):  # [start, stop)
    print(i)

# you can use range(start, stop, step) to create sequences of lists
sequence = list(range(10, 201, 10))  # [10, 201)
print(sequence)