
list = [1,2,3,4]
my_iter = iter(list)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
try:
    print(next(my_iter))
except StopIteration:
    print("all values exahusted")

