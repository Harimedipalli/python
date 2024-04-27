

list1 = [1,1,2,56]
list2 = [10,20,5,5,100]

total = 0
for i in range(len(list1)):
    total += list1[i] + list2[i]
print(total)


# Given lists
list1 = [1, 1, 2, 56]
list2 = [10, 20, 5, 5, 100]


# Find the minimum length between the two lists
min_length = min(len(list1), len(list2))
print(min_length)

# Initialize a variable to hold the sum
total_sum = 0

# Iterate over the lists and sum corresponding elements
for i in range(min_length):
    total_sum += list1[i] + list2[i]

# If one list is longer than the other, add the remaining elements
total_sum += sum(list1[min_length:]) + sum(list2[min_length:])

# Print the total sum
print("Sum of corresponding elements:", total_sum)
