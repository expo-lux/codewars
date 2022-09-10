import codewars_test as test

def prime_factors(n: int):
    res = ''
    base, pwr = 2, 0
    while n > 1:
        if n % base == 0:
            pwr += 1
            n = int(n / base)
            if n == 1:
                res += f"({base})" if pwr == 1 else f"({base}**{pwr})"
        else:
            if pwr > 0:
                res += f"({base})" if pwr == 1 else f"({base}**{pwr})"
            base += 1
            pwr = 0
    return res


@test.describe('Testing...')
def _():
    @test.it('Fixed tests')
    def _():
        test.assert_equals(prime_factors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
        test.assert_equals(prime_factors(2390549), "(7)(341507)")
