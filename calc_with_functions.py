# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
# kyu 5
import codewars_test as test
import operator


def zero(arg=0):
    return int(arg[0](0, arg[1])) if type(arg) == tuple else arg


def one(arg=1):
    return int(arg[0](1, arg[1])) if type(arg) == tuple else arg


def two(arg=2):
    return int(arg[0](2, arg[1])) if type(arg) == tuple else arg


def three(arg=3):  # your code here
    return int(arg[0](3, arg[1])) if type(arg) == tuple else arg

def four(arg=4):  # your code here
    return int(arg[0](4, arg[1])) if type(arg) == tuple else arg


def five(arg=5):  # your code here
    return int(arg[0](5, arg[1])) if type(arg) == tuple else arg


def six(arg=6):
    return int(arg[0](6, arg[1])) if type(arg) == tuple else arg


def seven(arg=7):  # your code here
    return int(arg[0](7, arg[1])) if type(arg) == tuple else arg


def eight(arg=8):  # your code here
    return int(arg[0](8, arg[1])) if type(arg) == tuple else arg


def nine(arg=9):  # your code here
    return int(arg[0](9, arg[1])) if type(arg) == tuple else arg


def minus(arg):
    return operator.sub, arg


def plus(arg):
    return operator.add, arg


def times(arg):
    return operator.mul, arg


def divided_by(arg):
    return operator.truediv, arg

test.describe('Basic Tests')
test.assert_equals(seven(times(five())), 35)
test.assert_equals(four(plus(nine())), 13)
test.assert_equals(eight(minus(three())), 5)
test.assert_equals(six(divided_by(two())), 3)