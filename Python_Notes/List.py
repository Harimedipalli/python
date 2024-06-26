"""

List:

    1. List is an collection of data type which is ordered and mutuable and indexed.
    2. Inside list we can perform curd operations.
    3. Enclosed with []
    4. Inside list we can access the elements with the index easily.

    Common built in operations like :
    append, extend, pop, remove, insert, index, count, reverse, sort, copy, len().

"""

# Append taked only one argument and will append the element at the end of the list.

l = [1,2,3,4]
l.append([5,6])
print(l)
l.append(5)
print(l)



# Extend will also add the elements at the end of the list but each element will be added in seperate index

e = [1,2,3,4]
e.extend([5,6,7])
print(e)


# pop will remove the element based on index

e.pop(5)
print(e)

# remove will remove the element based on the element value

e.remove(7)
print(e)

# insert will take 2 arguments. One is the index and second is the value that we are going to store in that index.

e.insert(5,6)
print(e)



# copy will be copy the object to another object reference will be the same, it is a shallow copy

print(id(e))
e.copy()
print(e)
print(id(e))

e.reverse()
print(e)
print(id(e))
# e.reverse()
# print(e)


e.sort()
print(e)
