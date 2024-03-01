

# Find the missing number

"""
Formula : Missing number = Total sum - Actual sum
            n * (n+1) // 2

"""


Numbers = [1, 2, 3, 4, 6, 7, 8]

# Caluclate the expected and actual sum

n = len(Numbers) + 1
Total_sum = n * (n+1) // 2
Actual_sum = sum(Numbers)

Missing_number = Total_sum-Actual_sum
print(Missing_number)



def find_missing_number(nums):
    """
    Finding the missing numbers
    :param nums:
    :return:
    """
    n1 = len(nums) + 1
    # Iterating over the range of numbers using range(1, n1+1) will see the number exists. if not will return the missing number.
    for i in range(1, n1+1):
        if i not in nums:
            return i
nums = [1,2,3,5,6,7,8]
result = find_missing_number(nums)
print(result)

