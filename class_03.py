"""
Following things we will cover today

1) Dictionary, list
2) Set, tuple
3) Conditional Statement

Assignments:
1) write a code to find maximum number from 5 values
2) write a code to find minimum number from 5 values
3) write a code to find maximum number from 10 values with only single if statement
4) write a code to find minimum number from 10 values with only single if statement

"""

blank_dict = dict()
# blank_dict['name'] = "Parth"
# blank_dict['number'] = 9876543221
#
# print('In Class 3 module: ', blank_dict)


# test_list = ['Parth']
# print(test_list)
# test_list.append('Shrikant')
# print(test_list)
#
# test_list.remove('Parth')
# print(test_list)

# test_list.pop(0)

# print(test_list.count('Parth'))
#
# print("Parth" in test_list)

# test_list.clear()

# _list = list()
# _dict = dict()
# _tuple = (2, 4, 65, (1, 4, 6))
# for i in _tuple:
#     print(i, type(i))
# print(_tuple, type(_tuple))

#
# my_dict = {
#     ('test',): 'what',
#     ('test',): 'exit',
#     'name': 'Parth',
#     'name': 'Parth Patel'
# }
#
# print(my_dict)

#
# _set_1 = [1,2,3,4,5,2,4,2,1,4,6,3,4,4,5,1,3,5,3,2,1,2,2,2,4]
# _set_2 = [3,4,5,2,2,4,5,5,2,3,3,4,32,42,6,]
#
# print(set(_set_1).difference(set(_set_2)))


"""
if
if else
# switch
if if else else
# <condition>: <positive>, <negative>
"""
no_1 = input("Enter No 1: ")
no_2 = input("Enter No 2: ")
no_3 = input("Enter No 3: ")

if no_1 < no_2:
    if no_3 < no_2:
        print("Max value is : ", no_2)
    else:
        print("Max value is : ", no_3)

elif no_1 < no_3:
    if no_3 < no_1:
        print("Max value is :", no_1)
    else:
        print("Max value is : ", no_3)

else:
    print("Are you serious about your inputs ?")


