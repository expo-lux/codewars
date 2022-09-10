import codewars_test as test
import re


def solution(s: str, markers: list):
    if markers:
        lines = s.split('\n')
        escaped = list(map(re.escape, markers))
        patterns = f"({'|'.join(escaped)})"
        res = [re.sub(r'\s*' + patterns + '.*$', '', line) for line in lines]
        return '\n'.join(res)
    else:
        return s


@test.describe('Test case')
def test_group():
    @test.it('Example')
    def test_case():
        test.assert_equals(solution('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']),
                           'apples, pears\ngrapes\nbananas')
        test.assert_equals(solution('a #b\nc\nd $e f g', ['#', '$']), 'a\nc\nd')
        test.assert_equals(solution(' a #b\nc\nd $e f g', ['#', '$']), ' a\nc\nd')
        test.assert_equals(solution(' a #b\nc\nd $e f g', []), ' a #b\nc\nd $e f g')
