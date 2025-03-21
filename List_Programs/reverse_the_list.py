#
# # Reversing the list
#
# print("First Logic")
#
#
# l = [7, 6, 5, 22, 3, 50, 23, 0, 0.2]
#
# length = len(l)  # length is 9
# print(length)
#
# # dividing the length of string and iterating it.
# for i in range(length // 2):
#     # Swap elements at positions i and length - i - 1
#     temp = l[i]
#     print(l[i])
#
#     l[i] = l[length - i - 1]
#     l[length - i - 1] = temp
# print(l)
#
#
#
#
# print("Second logic")
# l = [7, 6, 5, 22, 3, 50, 23, 0, 0.2]
#
# reverse_list = []
#
# for i in range(len(l) - 1, -1, -1):
#     reverse_list.append(l[i])
# print(reverse_list)
#
#
#
# print("Third logic")
#
# l = [7, 6, 5, 22, 3, 50, 23, 0, 0.2]
#
# start_index = 0
# end_index = len(l) - 1
#
# while start_index < end_index:
#     l[start_index], l[end_index] = l[end_index], l[start_index]
#
#     start_index += 1
#     end_index -= 1
# print(l)
#
#
#
# print("Fourth logic")
#
# l = [7, 6, 5, 22, 3, 50, 23, 0, 0.2]
#
# reverse_list = []
#
# for i in l[::-1]:
#     reverse_list.append(i)
# print(reverse_list)
#
#
# print("Fifth logic")
#
# l = [7, 6, 5, 22, 3, 50, 23, 0, 0.2]
#
# for _ in range(len(l)):
#     pop_element = l.pop()
#     l.insert(0, pop_element)
#
# print(l)


# def reverse_list(original_list) -> list :
#     reverse_list = []
#
#     for i in range(len(original_list) -1, -1, -1):
#         print(i)
#         reverse_list.append(original_list[i])
#     return reverse_list


# rs = (reverse_list([1,2,3,4,5]))
# print(rs)

def reverse_list(original_list):
    n = len(original_list)

    for i in range(n//2):
        original_list[i], original_list[n-i-1] = original_list[n-i-1], original_list[i]
    return original_list
rs = (reverse_list([1,2,3,4,5]))
print(rs)