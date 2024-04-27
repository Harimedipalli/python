

def my_dec(func):
    def inner_fucntion():
        print("first")
        func()
        print("third")
    return inner_fucntion()

@my_dec
def say_hello():
    print("second")

# say_hello()




l = [4,3,2,1]
start = 0
end = len(l) - 1
while start < end:
    l[start], l[end] = l[end], l[start]
    start += 1
    end -=1

print(l)






