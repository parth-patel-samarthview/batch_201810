"""
Following are the topics we will cover today.

0) Class  Part - 1
1) Iterator
2) Generator
3) Generator vs Iterator
4) Recursive Function

Assignment:
1) Factorial

"""

# #############################################################################
# 0) Class
# #############################################################################

"""
class <ClassName>(<Inheritance_class>):
    '''
    class epi-docs
    '''
    
    def __init__(self):
        '''
        Constructor 
        '''
    
    def <method_name>(self):
        '''
        Class method
        '''
        
"""


class MyClass(object):
    """
    This is my First class
    """

    def __init__(self):
        """
        Initializing class instance
        :param name: Pass name while initialize instance
        """
        self.name = None

    def greetings(self, name):
        self.name = name
        return F"Hello {name}"


# my_class = MyClass()
#
# my_class.class_name = "This is test"
#
# response = my_class.greetings(name="Parth")
#
# print(response)
#
#
# my_class2 = MyClass()
#
# response_2 = my_class2.greetings(name="Patel")
#
# print(response_2)

# #############################################################################
# 1) Iterator
# #############################################################################


# class MyRange:
#     """
#     my range function
#     """
#
#     def __init__(self, start=0, end=None, step=1):
#         self.start = start
#         self.end = end
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         if self.start < self.end:
#             i = self.start
#             self.start += self.step
#             return i
#         else:
#             raise StopIteration()
#
#     def previous(self):
#         if self.start < self.end:
#             i = self.start - (self.step * 2)
#             self.start -= self.step
#
#             return i
#         else:
#             raise StopIteration()

#
# data = MyRange(0, 5, 1)
#
# print(data.next())
# print(data.next())
# print(data.next())
# print(data.next())
# print(data.previous())
# print(data.next())
# print(data.next())

# #############################################################################
# 2) Generator
# #############################################################################


# def simple_generator():
#     start = 0
#     end = 5
#     while start < end:
#         yield start
#         start += 1
#
#
# for item in simple_generator():
#     print(item)

# -----------------------------------------------------
# def fib(limit):
#     # Initialize first two Fibonacci Numbers
#     a, b = 0, 1
#
#     # One by one yield next Fibonacci Number
#     while a < limit:
#         yield a
#         a, b = b, a + b
#         print("----", a, b)
#
#
# for i in fib(5):
#     print(i)

# -----------------------------------------------------
# def factorial(number):
#     output = 1
#     for i in range(1, number+1):
#         output *= i
#
#     return output
#
#
# print(factorial(4))


# #############################################################################
# 4) Recursive Function
# #############################################################################

# def prime(limit):
#     for no in range(1, limit + 1):
#         flag = True
#         for divider in range(2, no):
#             if no % divider == 0:
#                 flag = False
#                 break
#         if flag:
#             print(F"{no} is Prime.")
#
#
# def prime_re(start, limit):
#     if start == limit:
#         return
#
#     flag = True
#     for divider in range(2, start):
#         if start % divider == 0:
#             flag = False
#             break
#     if flag:
#         print(F"{start} is Prime.")
#
#     prime_re(start + 1, limit)
