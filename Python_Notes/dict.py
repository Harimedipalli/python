"""

    1. Dict is a un-ordered collection of items where each item is an key value pairs.
    2. Key must be unique and values can be any data type.
    3. keys are immutable and values are mutable.
    4. Dictionaries are mutable, meaning you can add, modify, or delete key-value pairs after the dictionary is created.
    5. key and value are seperated by :
    6. indicated by {}
    7. can be accessed by keys.

'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

"""

d = {"name": "hari", "age":23}
print(dir(d))

print(d.pop("age"))
print(d)


# It will update the value if present if not will insert if not exists.

print(d.setdefault("age", 27))
print(d)

print(d.setdefault("city","bnglre"))
print(d)



print(d.update({"age":23}))
print(d)

print(d.update({"state":"karnataka"}))
print(d)







