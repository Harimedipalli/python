# Removing the duplicates from list
from operator import index

Duplicate_list = [1, 1, "a", "a", 0.5, 0.5, 22, 22, 56, 56, 5, 2, 9]

Non_Duplicate_list = []

for i in Duplicate_list:
    if i not in Non_Duplicate_list:
        Non_Duplicate_list.append(i)
print(Non_Duplicate_list)



Duplicate_list = [1, 1, "a", "a", 0.5, 0.5, 22, 22, 56, 56, 5, 2, 9]

Unique_list = list(set(Duplicate_list))

print(Unique_list)



Duplicate_list = [1, 1, "a", "a", 0.5, 0.5, 22, 22, 56, 56, 5, 2, 9]
unique_list = {}

for item in Duplicate_list:
    unique_list[item] = None
unique_list = list(unique_list.keys())

print(unique_list)


index = 0
unique_list = {}
for num in Duplicate_list:
    if num not in unique_list.values():
        unique_list[index] = num
        index = index + 1
print(unique_list)

print("Hello world")