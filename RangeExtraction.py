# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
import codewars_test as test
from itertools import islice

def solution(args: list):
    def append_to_result(start, length):
        if length == 1:
            res.append(str(args[start]))
        elif length == 2:
            res.append(str(args[start]))
            res.append(str(args[start + 1]))
        elif length > 2:
            res.append(str(args[start]) + '-' + str(args[start + length - 1]))

    res, i = [], 0
    while True:
        try:
            a = iter(range(args[i], args[-1] + 1))
            it = islice(args, i, len(args) + 1)
            count = 0
            while next(a) == next(it):
                count += 1
            append_to_result(i, count)
            i += count
        except StopIteration:
            append_to_result(i, count)
            break
    return ",".join(res)


test.describe("Sample Test Cases")

test.it("Simple Tests")
# test.assert_equals(solution([-6, -3]),
#                    '-6,-3-1')
test.assert_equals(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]),
                   '-6,-3-1,3-5,7-11,14,15,17-20')
test.assert_equals(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]), '-3--1,2,10,15,16,18-20')
