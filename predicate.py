#https://www.codewars.com/kata/626a887e8a33feabd6ad8f25
# Hmmmm, how do we go about this...
# You decide!

def predicate():
    pass

# class predicate:
#     ...
#
# predicate = ...

import codewars_test as test


@test.describe("Examples from the description")
def describe():
    @test.it("1 argument")
    def it():
        @predicate
        def is_even(num):
            return num % 2 == 0

        @predicate
        def is_positive(num):
            return num > 0

        test.assert_equals((is_even & is_positive)(4), True)
        test.assert_equals((is_even & is_positive)(3), False)
        test.assert_equals((is_even | is_positive)(3), True)
        test.assert_equals((~is_even & is_positive)(3), True)

    @test.it("0 arguments")
    def it():
        @predicate
        def to_be():
            return True

        test.assert_equals((to_be | ~to_be)(), True)

    @test.it("2 arguments, keyword arguments")
    def it():
        @predicate
        def is_equal(a, b):
            return a == b

        @predicate
        def is_less_than(a, b):
            return a < b

        test.assert_equals((is_less_than | is_equal)(1, 2), True)
        test.assert_equals((is_less_than | is_equal)(2, b=2), True)
        test.assert_equals((is_less_than | is_equal)(a=3, b=2), False)

    @test.it("should be callable and behave like the original")
    def it():
        @predicate
        def is_less_than(a, b):
            return a < b

        test.assert_equals(is_less_than(1, 2), True)
        test.assert_equals(is_less_than(2, 2), False)
        test.assert_equals(is_less_than(3, 2), False)