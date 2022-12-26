# https://www.codewars.com/kata/54d81488b981293527000c8f
# 5 kyu

import codewars_test as test


def sum_pairs(l: list, total) -> list:
    additionals = set()
    for item in l:
        if item in additionals:
            return [total - item, item]
        else:
            additionals.add(total - item)


# groupby - perhaps it even faster
# from itertools import groupby
# groups = list(groupby(l))
# result, minimal = [], len(groups)
# for i, item1 in enumerate(groups):
#     if i > minimal:
#         break
#     for k, item2 in enumerate(groups[i+1:]):
#         s = item1[0] + item2[0]
#         if s == total and k < minimal:
#             result = [item1[0], item2[0]]
#             if k == i+1:
#                 return result
#             minimal = k
# return result if result else None

# invalid attempt
# res = []
# minimal = len(l)
# for i, val1 in enumerate(l):
#     if i > minimal:
#         break
#     for k, val2 in enumerate(l[i+1:]):
#         s = val1 + val2
#         if s == total and k < minimal:
#             res = [val1, val2]
#             if k == i+1:
#                 return res
#             minimal = k
# return res if res else None

@test.describe("Sample Tests")
def sample_tests():
    l1 = [1, 1, 4, 8, 7, 3, 15]
    l2 = [1, -2, 3, 0, -6, 1]
    l3 = [20, -13, 40]
    l4 = [1, 2, 3, 4, 1, 0]
    l5 = [10, 5, 2, 3, 7, 5]
    l6 = [4, -2, 3, 3, 4]
    l7 = [0, 2, 0]
    l8 = [5, 9, 13, -3]
    l9 = [1] * 10000000
    l9[len(l9) // 2 - 1] = 6
    l9[len(l9) // 2] = 7
    l9[len(l9) - 2] = 8
    l9[len(l9) - 1] = -3
    l9[0] = 13
    l9[1] = 3

    @test.it("Tests")
    def _():
        test.assert_equals(sum_pairs(l1, 8), [1, 7], "Basic: %s should return [1, 7] for sum = 8" % l1)
        test.assert_equals(sum_pairs(l2, -6), [0, -6], "Negatives: %s should return [0, -6] for sum = -6" % l2)
        test.expect(sum_pairs(l3, -7) is None, "No Match: %s should return None for sum = -7" % l3)
        test.assert_equals(sum_pairs(l4, 2), [1, 1], "First Match From Left: %s should return [1, 1] for sum = 2 " % l4)
        test.assert_equals(sum_pairs(l5, 10), [3, 7],
                           "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
        test.assert_equals(sum_pairs(l6, 8), [4, 4], "Duplicates: %s should return [4, 4] for sum = 8" % l6)
        test.assert_equals(sum_pairs(l7, 0), [0, 0], "Zeroes: %s should return [0, 0] for sum = 0" % l7)
        test.assert_equals(sum_pairs(l8, 10), [13, -3], "Subtraction: %s should return [13, -3] for sum = 10" % l8)
        test.assert_equals(sum_pairs(l9, 13), [6, 7],
                           "Ten Million Numbers With Middle Pair: Should terminate with a valid pair output")
        test.assert_equals(sum_pairs(l9, 5), [8, -3],
                           "Ten Million Numbers With Pair At End: Should terminate with a valid pair output")
        test.assert_equals(sum_pairs(l9, 16), [13, 3],
                           "Ten Million Numbers With Pair At Start: Should terminate with a valid pair output")
        test.expect(sum_pairs(l9, 31) is None,
                    "Ten Million Numbers With No Match: Should return None in a decent time period")
