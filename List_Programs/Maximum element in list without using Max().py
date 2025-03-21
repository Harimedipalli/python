# Find the maximum element in a list without max()

list_of_elements = [10,12,20,22,30,33,40,44,50,55]

def max_ele(largest_number):
    # Assume the first element of the list is the largest.
    max_num = largest_number[0]
    larget = []
    # loop the element in list to compare largest value
    for num in largest_number:
        # Compare every element in the list with the current largest value.
        if num > max_num:
            # If you find a bigger element, update your largest value
            max_num = num
            # Keep checking until you reach the last element
    # The largest value you found is the maximum element.
    print(max_num)

largest_number = [10,12,20,22,30,33,40,44,50,55]
max_ele(largest_number)


result = min(largest_number)
print(result)
