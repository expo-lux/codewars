# https://www.codewars.com/kata/54da5a58ea159efa38000836
import codewars_test as test


def find_it(seq):
    d = {}
    for item in seq:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    for k, v in d.items():
        if v % 2:
            return k


@test.describe("Sample tests")
def sample_tests():
    @test.it("find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) should return 5 (because it appears 3 times)")
    def _():
        test.assert_equals(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)

    @test.it("find_it([1,1,2,-2,5,2,4,4,-1,-2,5]) should return -1 (because it appears 1 time)")
    def _():
        test.assert_equals(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]), -1);

    @test.it("find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]) should return 5 (because it appears 3 times)")
    def _():
        test.assert_equals(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]), 5);

    @test.it("find_it([10]) should return 10 (because it appears 1 time)")
    def _():
        test.assert_equals(find_it([10]), 10);

    @test.it("find_it([10, 10, 10]) should return 10 (because it appears 3 times)")
    def _():
        test.assert_equals(find_it([10, 10, 10]), 10);

    @test.it("find_it([1,1,1,1,1,1,10,1,1,1,1]) should return 10 (because it appears 1 time)")
    def _():
        test.assert_equals(find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]), 10);

    @test.it("find_it([5,4,3,2,1,5,4,3,2,10,10]) should return 1 (because it appears 1 time)")
    def _():
        test.assert_equals(find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]), 1);
