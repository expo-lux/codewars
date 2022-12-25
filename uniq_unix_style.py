# https://www.codewars.com/kata/52250aca906b0c28f80003a1
# 5 kyu

import codewars_test as test


def uniq_c(seq):
    result = []
    if seq:
        prev = seq[0], 1
        for item in seq[1:]:
            if item == prev[0]:
                prev = prev[0], prev[1] + 1
            else:
                result.append(prev)
                prev = item, 1
        result.append(prev)
    return result


# optimal solution
# from itertools import groupby
#
# def uniq_c(seq):
#     return [(k, len(list(v))) for k, v in groupby(seq)]


@test.describe('Example Tests')
def example_tests():
    test.assert_equals(uniq_c(['a', 'a', 'b', 'b', 'c', 'a', 'b', 'c']),
                       [('a', 2), ('b', 2), ('c', 1), ('a', 1), ('b', 1), ('c', 1)])
    test.assert_equals(uniq_c(['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']), [('a', 3), ('b', 3), ('c', 3)])
    test.assert_equals(uniq_c([None, 'a', 'a']), [(None, 1), ('a', 2)])
    test.assert_equals(uniq_c(['foo']), [('foo', 1)])
    test.assert_equals(uniq_c(['']), [('', 1)])
    test.assert_equals(uniq_c([]), [])
