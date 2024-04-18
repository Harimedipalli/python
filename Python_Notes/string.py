"""

    1.string is a sequeance of characters enclosed with     `

"""


# f = open("C:\\Users\HP\Desktop\demo.txt", "w")
# f.write("dont worry")
# f.close()
#
#
# f = open("C:\\Users\HP\Desktop\demo.txt", "a")
# f.write("adding nrew line please have a look")
# f.close()
#
# f = open("C:\\Users\HP\Desktop\demo.txt", "r")
# print(f.read())



try:
    f = open("C:\\Users\HP\Desktop\demo.txt", "r")
    content = f.read()
    print(content)
except FileNotFoundError as e:
    print("execpction as ", e)
finally:
    if 'file' in locals():
        f.close()
    print("file closed if opened")





try:
    x = 10
    y = 0
    res = x/y
    print("result", res)
except Exception as e:
    print("Error:", e)

x = 10
y = 0
res = x/y
print("result", res)
