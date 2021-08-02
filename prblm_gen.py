def my_gen(a):
    for i in a:
        print("Generator loop")
        yield i

a =my_gen([1, 2, 5, 7, 9])
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

# import pdb;pdb.set_trace()
#
# for i in my_gen([1, 2, 5, 7, 9]):
#     print("Normal for loop")
#     print(i)

