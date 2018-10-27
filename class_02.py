"""
Following things we will cover today

1) Variable
2) String, Integer, Boolean Data Type
3) None Type
4) List, Dictionary

"""

# #############################################################################
# 1) Variable
# #############################################################################

""""""
batch_10_str = "Parth, Sreekant,..."
# print(batch_10_str, type(batch_10_str), id(batch_10_str), id(type(batch_10_str)))

batch_10_int = 9
# print(batch_10_int, type(batch_10_int), id(batch_10_int))

batch_10_bool = False
# print(batch_10_bool, type(batch_10_bool), id(batch_10_bool))

batch_10_none = None
# print(batch_10_none, type(batch_10_none), id(batch_10_none))


x = str()
# print(x, type(x), id(x), id(type(x)))

batch_10_std = ['Sreekant', 'Parth', 'Babasaheb', 'Dadasaheb']

batch_10_list = [
    batch_10_str, batch_10_int, batch_10_bool, batch_10_none, x,
    ['test', 909, 10.5, [batch_10_str]]
]

# print(batch_10_list)
#
# print(batch_10_std[0:3])
# print(batch_10_std[0:3:2])

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_numbers[9::2])
# print(list_numbers[7:2:-1])
# print(list_numbers[11::-1])
# print(list_numbers[9::0])
# print(list_numbers[11::])

# for(i=0; i<=10; i=i+2){}

batch_10_dict = {
    'name': 'sreekant',
    'profession': 'student',
    'salary': 3000000,
    'dept': batch_10_list
}

batch_10_dict['name'] = 'test'
print(batch_10_dict)