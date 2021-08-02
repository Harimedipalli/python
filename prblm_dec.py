def student_dec(college):
    def inner_function(*args):
        # print('he is from {guntur}')
        college(args[0])
        for i in args[1:]:
            # print(f'{i} is from guntur')

            print(f'\t Student name:\t {i} ')
        return f"{args[0]} student detalis listed above"

    return inner_function


@student_dec
def college1(name):
    print(f'College name is {name}')


# @student_dec
# def college2(name):
#     print(f'college name is {name}')


print(college1('khit', 'sai', 'hari'))
print(college1('bec', 'srikant', 'mahesh'))
