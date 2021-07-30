l = [
    {'Name': 'Srikanth', 'MobileNo': 9618114079, 'Salary': 10000},
    {'Name': 'Sai', 'MobileNo': 8787890909, 'Salary': 50000},
]
name = 'maheswar';
mob = 3253236;
sal = 3434
l.append({'Name': 'mahesh', 'MobileNo': 1234665, 'Salary': 3434})

print(l)
print('before updating l')


def update_mobileno(name, new_mobile):
    for i in l:
        if i['Name'] == name:
            i.update({'MobileNo': new_mobile})
            return "update susscesful "


da = update_mobileno("mahesh", 68766887)
print(da)
print('after updating the record l')
print(l)

print('delete method started')


def delete_record(name):
    for k in range(len(l)):
        print(l[k])
        if l[k]['Name'] == name:
            l.pop(k)
            return 'deletion done'


dd = delete_record('Sai')
print(dd)

print(l)

print('adding record starts')


# def verify(record):
#     for h in range(len(l)):
#         if l[h]['Name'] == record['Name']:
#             return True
#     return False


def add_record(record):
    #   if not verify(record):
    #import pdb;pdb.set_trace()
    if not any([i['Name'] == record['Name'] for i in l]):
        #import pdb
        l.append(record)
        print('sucessfully added the record')

    else:
        print("record already exits with {}".format(record['Name']))

add_record({'Name': 'Nani', 'MobileNo': 9618111542})
print(l)
add_record({'Name': 'Nani', 'MobileNo': 9618111542})
