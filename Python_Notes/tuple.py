"""

    1. Tuple is an ordered data type which is immutable.
    2. Cant perform curd operations.
    3. can be defined by ()
    4. when you want to store a fixed sequence of elements that should not be modified throughout the program.
    5.

    count, index
"""

t = (1,2,3,4)
len(t)
print(dir(t))

print(t.count(2))

print(t.index(1))

print(t[2:6])

