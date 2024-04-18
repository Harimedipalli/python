numbers = [3,44,2,1,34,11,45,6]


large = numbers[0]
small = numbers[0]

for num in numbers:
    if num > large:
        large = num
        print("max")
    elif num < small:
        small = num
        print("min")
print(large)
print(small)


largest = max(numbers)
smallest = min(numbers)

print(largest,smallest)
