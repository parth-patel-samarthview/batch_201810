"""
1) Looping Statement
2) Conditional and looping Statement

Assignment:
Create pattern using for or while loop
1)                  2)              3)              4)
* * * * *           1 1 1 1 1       0 0 0 0 0       0
* * * * *           1 1 1 1 1       1 1 1 1 1       1 0
* * * * *           1 1 1 1 1       0 0 0 0 0       0 1 0
* * * * *           1 1 1 1 1       1 1 1 1 1       1 0 1 0
* * * * *           1 1 1 1 1       0 0 0 0 0       0 1 0 1 0

5)                  6)              7)                  8)
1                   1 2 3 4 5       01 02 03 04 05      1 0 1 0 1
1 0                 1 2 3 4 5       06 07 08 09 10      0 1 0 1
1 0 1               1 2 3 4 5       11 12 13 14 15      1 0 1
1 0 1 0             1 2 3 4 5       16 17 18 19 20      0 1
1 0 1 0 1           1 2 3 4 5       21 22 23 24 25      1

9)                  10)             11)                 12)
      1             * *   * *       01 02 03 04 05      2
   1    1           *  * *  *       05 04 03 02 01      2 4
  1   1   1         *   *   *       02 04 06 08 10      2 4 8
1   1   1   1       *       *       10 08 06 04 02      2 4 8 16
                    *       *       03 06 09 12 15      2 4 8 16 32
                                    15 12 09 06 03      2 4 8 16 32 64

13) *       *
    * *   * *
    *   *   *
    *       *
    *       *

1) Create a Matrix
2) Matrix Multiplication
3) Spiral Matrix rotation
4) Shift elements in Matrix


"""

# Looping statement
# # while
# # for
# # Comprehension

# no = 1
# while no <= 10:
#     print(no)
#     no += 1

"""
no = 1
while True:
    if no == 11:
        break

    no += 1
    if no % 2 == 0:
        continue

    print(no)
    # no += 1

"""

batch_10_std = ['Sreekant', 'Parth', 'Babasaheb', 'Dadasaheb']

batch_10_dict = {
    'name': 'sreekant',
    'profession': 'student',
    'salary': 3000000,
    'dept': ['test']
}

for i in range(10, 0, -1):
    print(i)

for i in range(0, 4):
    print(batch_10_std[i])

for i in batch_10_std:
    print(i)


for index, value in enumerate(batch_10_std):
    print(index, value)


matrix = list()
for i in range(0,3):
    row = []
    for j in range(0, 3):
        row.append(j)
    matrix.append(row)

print(matrix)
"""
Output: 

[
    [0, 1, 2], 
    [0, 1, 2], 
    [0, 1, 2]
]
"""


for key, value in batch_10_dict.items():
    # print("Key: " + key + " value: " + value)
    # print("Key: {} value: {}".format(key, value))
    # print("Key: {key} value: {value}".format(key=key, value=value))
    print(F"Key: {key} value: {value}")


