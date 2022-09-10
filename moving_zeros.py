# https://www.codewars.com/kata/52597aa56021e91c93000cb0
# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other
# elements.

#OMG!!!!!
#def move_zeros(array):
#    return [x for x in array if x] + [0]*array.count(0)

import codewars_test as test


def move_zeros(lst: list):
    def move_to_end(idx: int):
        for pos in range(idx, len(lst) - 1):
            lst[pos], lst[pos + 1] = lst[pos + 1], lst[pos]

    i = zero_count = 0
    if lst:
        while True:
            if lst[i] == 0:
                move_to_end(i)
                zero_count += 1
            else:
                i += 1
            if i == len(lst) - zero_count:
                break
    return lst


@test.it("Basic tests")
def youarecute():
    test.assert_equals(move_zeros(
        [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
        [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
    test.assert_equals(move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    test.assert_equals(move_zeros([0, 0]), [0, 0])
    test.assert_equals(move_zeros([0]), [0])
    test.assert_equals(move_zeros([]), [])
