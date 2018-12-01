"""

1) Function with no argument and no Return value
2) Function with no argument and with Return value
3) Function with argument and No Return value
4) Function with argument and Return value
5) Function with wild card arguments
6) Lambda Function


Assignment:
1) Convert your all previous assignment in function
2) Prepare Calculator with function
   (Addition, Subtraction, Multiplication, division)
3) Merge 2 dictionary

"""

"""
def <function_name>():
    '''
    Function epi-docs 
    '''
    <function statement>
"""


def greetings():
    """
    Greet world
    :return:
    """
    print("hello World")


def greetings_with_args(name):
    """
    Greet requested user
    :param name: user name
    :return:
    """
    print(F'Hello {name}')


def greetings_return():
    """
    Return Greetings
    :return:
    """
    return 'Hello World'


def greetings_args_return(name):
    """
    Return Greetings
    :return:
    """
    return F'Hello {name}'


def greetings_list_wild(*args):
    """
    Greetings wild card argument
    :param args:
    :return:
    """
    return F"Hello {args}"


def greetings_dict_wild(**kwargs):
    """

    :param kwargs:
    :return:
    """

    return F"Hello {kwargs.get('name', '')}"


def _greetings(name="World"):
    """

    :param name:
    :return:
    """
    print(F"Hello {name}")


x = lambda y: y*y  # this function for return

print(x(5))