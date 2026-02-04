print("Print every number from 0 - 4:")
# range(n) prints every number from 0 to n - 1.
# Print every number from 0 - 4
for i in range(5):  # [0, 5)
    print(i)

print("Print every number from 1 - 5:")
# Print every number from 1 - 5
for i in range(5):
    print(i + 1)

# range(n) [0, n - 1]
# [0, n)

print("Print every number from 2 - 6")
# range(x, y) prints every number from x to y - 1.
# range(x, y) [x, y)
# [x, y - 1]
for i in range(2, 7): # [2, 7)
    print(i)

print("Print every number from 4 - 5")
for i in range(4, 6): # [4, 6)
    print(i)

# You can turn a range into a list to see all the values at once.
nums = list(range(6))  # [0, 6)
print(nums)

nums2 = list(range(10, 101)) # [10, 101)
print(nums2)