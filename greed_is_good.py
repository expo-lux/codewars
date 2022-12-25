# https://www.codewars.com/kata/5270d0d18625160ada0000e4 (5)
import codewars_test as test


def score(dice: list):
    triple_scores = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600, 1: 1000}
    single_scores = {1: 100, 5: 50}

    def find_triple(arr: list):
        counts = list(arr.count(i) for i in range(1, 7))
        for i in range(3, 6):
            try:
                res = counts.index(i) + 1
                return res
            except ValueError:
                pass
        return 0

    def remove_triple(arr: list, value: int):
        try:
            for i in range(3):
                arr.remove(value)
        except:
            pass

    points, temp_list = 0, dice.copy()
    if triple := find_triple(temp_list):
        points += triple_scores[triple]
        remove_triple(temp_list, triple)
    points += sum(temp_list.count(i) * single_scores[i] for i in [1, 5])
    return points


# your code here


test.describe("Example Tests")
test.it("Example Case")
test.assert_equals(score([3, 3, 3, 3, 3]), 300)
test.assert_equals(score([1, 1, 1, 1, 3]), 1100)
test.assert_equals(score([1, 1, 1, 1, 5]), 1150)
