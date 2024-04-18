# def find_majority_element(elements):
#     candidate = None
#     count = 0
#
#     for element in elements:
#         if count == 0:
#             candidate = element
#             count = 1
#         elif candidate == element:
#             count += 1
#         else:
#             count -= 1
#
#     # Verify if the candidate is the majority element
#     count = 0
#     for element in elements:
#         if element == candidate:
#             count += 1
#
#     if count > len(elements) // 2:
#         return candidate
#     else:
#         return None
#
# # Given list
# elements = [2, 3, 4, 5, 2, 2, 2, 6, 2, 2, 7]
#
# # Find the majority element
# majority_element = find_majority_element(elements)
#
# # Print the result
# if majority_element is not None:
#     print("The majority element is:", majority_element)
# else:
#     print("There is no majority element in the list")










# Corrected input list with a majority element
# Corrected input list with a majority element
elements = [2, 3, 4, 5, 2, 2, 2, 6, 2, 2, 7, 4, 2, 4, 5, 3, 3, 6, 7, 2, 2, 2, 2]




for element in set(elements):
    count = elements.count(element)

    if count > len(elements)//2:
        print("majority is", element)
        break
else:
    print("no majority")


# Given list
elements = [2, 3, 4, 5, 2, 2, 2, 6, 2, 2, 7]


# Iterate over each unique element in the list
for element in set(elements):
    # Count the occurrences of the current element
    count = elements.count(element)
    # Check if the count is greater than half the length of the list
    if count > len(elements) // 2:
        print("The majority element is:", element)
        break
else:
    print("There is no majority element in the list")




elements = [2, 3, 4, 5, 2, 2, 2, 6, 2, 2, 7, 4, 2, 4, 5, 3, 3, 6, 7, 2, 2, 2, 2]

ele_count = {}

for element in elements:
    if element in ele_count:
        ele_count[element] += 1
    else:
        ele_count[element] =1
print(ele_count)

total_count =  sum(ele_count.values())
print("Total count:", total_count)

for element, count in ele_count.items():
    if count > total_count // 2:
        print("maajority element is ", element)
        break
else:
    print("no majority")









