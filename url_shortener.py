# https://www.codewars.com/kata/5fee4559135609002c1a1841
# 5 kuy

class Url_shortener:

    def __init__(self):
        self.__counter = -1
        self.__long = {}
        self.__short = {}

    def shorten(self, long_url):
        if long_url in self.__short:
            return self.__short[long_url]
        else:
            self.__counter += 1
            if self.__counter < 26 ** 4:
                val = self.__counter
                d1 = val // (26 ** 3)
                val -= d1 * (26 ** 3)
                d2 = val // (26 ** 2)
                val -= d2 * (26 ** 2)
                d3 = val // 26
                val -= d3 * 26
                d4 = val
                k = "short.ly/" + chr(d1 + 97) + chr(d2 + 97) + chr(d3 + 97) + chr(d4 + 97)
            elif 26 ** 4 <= self.__counter < 26 ** 4 + 26:
                val = self.__counter - 26 ** 4
                k = "short.ly/" + chr(val + 97)
            elif 26 ** 4 + 26 <= self.__counter < 26 ** 4 + 26 + 26 ** 2:
                val = self.__counter - (26 ** 4 + 26)
                d1 = val // 26
                val -= d1 * 26
                d2 = val
                k = "short.ly/" + chr(d1 + 97) + chr(d2 + 97)
            elif 26 ** 4 + 26 + 26 ** 2 <= self.__counter < 26 ** 4 + 26 + 26 ** 2 + 26 ** 3:
                val = self.__counter - (26 ** 4 + 26 ** 2 + 26)
                d1 = val // (26 ** 2)
                val -= d1 * (26 ** 2)
                d2 = val // 26
                val -= d2 * 26
                d3 = val
                k = "short.ly/" + chr(d1 + 97) + chr(d2 + 97) + chr(d3 + 97)
            self.__short[long_url] = k
            self.__long[k] = long_url
            return k

    def redirect(self, short_url):
        return self.__long[short_url]


import codewars_test as test
import re


def test_format(string):
    return re.search("^short.ly\/[a-z]{1,4}$", string)


@test.describe("Should pass all of these")
def tests():
    @test.it("Testing two different URLs")
    def test_different():
        url_shortener = Url_shortener()
        short_url1 = url_shortener.shorten("https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e")
        test.expect(test_format(short_url1), message="Wrong format!")
        short_url2 = url_shortener.shorten("https://www.codewars.com/kata/5efae11e2d12df00331f91a6")
        test.expect(test_format(short_url2), message="Wrong format!")
        test.assert_equals(url_shortener.redirect(short_url1),
                           "https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e")
        test.assert_equals(url_shortener.redirect(short_url2),
                           "https://www.codewars.com/kata/5efae11e2d12df00331f91a6")

    @test.it("Testing same URLs")
    def test_same():
        url_shortener = Url_shortener()
        short_url1 = url_shortener.shorten("https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f")
        test.expect(test_format(short_url1), message="Wrong format!")
        short_url2 = url_shortener.shorten("https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f")
        test.expect(test_format(short_url2), message="Wrong format!")
        test.assert_equals(short_url1, short_url2, message="Should work with same long URLs")
        test.assert_equals(url_shortener.redirect(short_url1),
                           "https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f")
