# https://www.codewars.com/kata/52685f7382004e774f0001f7
# 5 kyu
import codewars_test as test


def make_readable(seconds):
    def readable(v: int) -> str:
        return "0" + str(v) if v <= 9 else str(v)

    val = seconds
    hours = seconds // 3600
    val -= hours * 3600
    minutes = val // 60
    val -= minutes * 60
    seconds = val % 60
    return f"{readable(hours)}:{readable(minutes)}:{readable(seconds)}"


test.assert_equals(make_readable(0), "00:00:00")
test.assert_equals(make_readable(5), "00:00:05")
test.assert_equals(make_readable(60), "00:01:00")
test.assert_equals(make_readable(86399), "23:59:59")
test.assert_equals(make_readable(359999), "99:59:59")
