#https://www.codewars.com/kata/5839c48f0cf94640a20001d3
#5 kyu
import codewars_test as test


def land_perimeter(table: list):
    def scanline(s):
        r = []
        temp = ''
        for c in s:
            if c == 'X':
                temp += c
            else:
                if temp:
                    r.append(temp)
                    temp = ''
        return sum(2 * len(x) - 2 for x in r)

    arr = table.copy()
    size = len(arr[0]) + 2
    arr.insert(0, 'O' * size)
    arr.append('O' * size)
    for i, item in enumerate(arr):
        arr[i] = 'O' + arr[i] + 'O'
    x1 = sum(scanline(line) for line in arr)  # horizontal scan
    cols = list(zip(*arr))
    x2 = sum(scanline(col) for col in cols)
    res = sum(line.count('X') for line in arr) * 4 - x1 - x2
    return f"Total land perimeter: {res}"

test.describe("Basic tests")

test.assert_equals(land_perimeter(
    ["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]),
                   "Total land perimeter: 60")
test.assert_equals(
    land_perimeter(["OXOOO", "OOXXX", "OXXOO", "XOOOO", "XOOOO", "XXXOO", "XOXOO", "OOOXO", "OXOOX", "XOOOO", "OOOXO"]),
    "Total land perimeter: 52")
test.assert_equals(land_perimeter(["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"]),
                   "Total land perimeter: 40")
test.assert_equals(land_perimeter(["XOOOXOO", "OXOOOOO", "XOXOXOO", "OXOXXOO", "OOOOOXX", "OOOXOXX", "XXXXOXO"]),
                   "Total land perimeter: 54")
test.assert_equals(land_perimeter(["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"]),
                   "Total land perimeter: 40")
