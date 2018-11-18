"""
1) Comprehension
2) Indentation, scope of variable & section
3) Built-in Functions: min, max, count, len, split, zip, types, sum, sorted

Assignment:

1) create matrix using comprehension
Output: [[0, 1, 2],[0, 1, 2],[0, 1, 2]]

2) Write a program to create dictionary of name, salary, designation from list
example: ['parth', 20000, 'Programmer']
output = {'name':'parth', 'designation':'Programmer', 'salary':20000}

3) Write a program to create list of dictionary to store user info
example: [['parth', 20000, 'Programmer'], ['Srikant', 50000, 'Sr. Programmer']]
output = [
    {'name':'parth', 'designation':'Programmer', 'salary':20000},
    {'name':'Srikant', 'designation':' Sr. Programmer', 'salary':50000}
]

"""
# #############################################################################
# 1) List and Dictionary Comprehension
# #############################################################################
#
number = [i * i for i in range(0, 5)]
print(number)

_number = []
for i in range(0, 5):
    _number.append(i * i)

print(_number)


odds = [
    i for i in range(1, 10, 2)
]

print(odds)


threes = [i for i in range(1, 30) if i % 3 == 0]

print(threes)
for i in range(1, 30):
    if i % 3 == 0:
        print(i)


powers = {"Power of {i}": i * i for i in range(0, 5)}
print(powers)

_powers = {}
for i in range(0,5):
    _powers[i] = i*i

print(_powers)


# #############################################################################
# 3) Built-in Functions: min, max, count, len, split, zip, type, sum, sorted
# #############################################################################


# Min
x = [1, 3, 1, 4, 6, 3, 45, 67, 83, 3, 111, 45]

print(F"Minimum value {min(x)}")

print(F"Maximum value {max(x)}")

print(F"1 appears in x list: {x.count(0)} time/s")

print(F"Total elements in x is {len(x)}")

para = "This is Samarthview. We all are here for learn python. I don't know python."

split_string = ". "
print(para.split(split_string))

# ###########
# zip
# ###########
headers = ['name', 'location', 'native']
data_1 = ['Parth', 'Pune', 'Home']
data_2 = ['Parth2', 'Pune', 'Home2']

for z, v, w in zip(headers, data_1, data_2):
    print(z, v, w)


dict_1 = {'x': 5, 'y': 2}
dict_2 = {'x': 4, 'y': 5}

for dic1, dic2 in zip(dict_1.items(), dict_2.items()):
    if dic1[1] > dic2[1]:
        break
    print(dic1[1], dic2[1])


list_of_number = [1, 3, 1, 4, 6, 3, 45, 67, 83, 3, 111, 45]

print(sum(list_of_number))

print(sorted(list_of_number))

dictionary = {'z': 97, 'r': 98, 'x': 99, 'a': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'w': 114}

print(sorted(dictionary.items(), reverse=True))


print(zip(dictionary, list_of_number))

dictionary['s'] = 5

dictionary.update({
    'rr': 'rr', 'dd': 'ere'
})
