# str1 = "srikanth"
# # ['srikanth','rikanth','ikanth','kanth','anth','nth','th','h']
# str2=[]
#
# for index in range(len(str1)):
#      str2.append(str1[index:])
# print(str2)
#
#


s='Hari'

for i in range(len(s)):
    for j in range(len(s)):
        print(" ", end=' ')
        for j in range(i + 1):
            print(s[j], end='')
    print('\n')
