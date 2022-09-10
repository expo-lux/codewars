# https://www.codewars.com/kata/52ebe4608567ade7d700044a
#dict generator: awk '{print ""$2"c:"$1""}' 1.txt | awk -F ':' '{print "\x27"$1"\x27:\x27"$2"\x27"}' | tr '\n' ','
def encode(cards: list):
    dic = {'Ac': 0, '2c': 1, '3c': 2, '4c': 3, '5c': 4, '6c': 5, '7c': 6, '8c': 7, '9c': 8, 'Tc': 9, 'Jc': 10, 'Qc': 11,
           'Kc': 12, 'Ad': 13, '2d': 14, '3d': 15, '4d': 16, '5d': 17, '6d': 18, '7d': 19, '8d': 20, '9d': 21, 'Td': 22,
           'Jd': 23, 'Qd': 24, 'Kd': 25, 'Ah': 26, '2h': 27, '3h': 28, '4h': 29, '5h': 30, '6h': 31, '7h': 32, '8h': 33,
           '9h': 34, 'Th': 35, 'Jh': 36, 'Qh': 37, 'Kh': 38, 'As': 39, '2s': 40, '3s': 41, '4s': 42, '5s': 43, '6s': 44,
           '7s': 45, '8s': 46, '9s': 47, 'Ts': 48, 'Js': 49, 'Qs': 50, 'Ks': 51}
    return sorted([dic[item] for item in cards])


def decode(cards):
    dic = {0: 'Ac', 1: '2c', 2: '3c', 3: '4c', 4: '5c', 5: '6c', 6: '7c', 7: '8c', 8: '9c', 9: 'Tc', 10: 'Jc', 11: 'Qc',
           12: 'Kc', 13: 'Ad', 14: '2d', 15: '3d', 16: '4d', 17: '5d', 18: '6d', 19: '7d', 20: '8d',
           21: '9d', 22: 'Td', 23: 'Jd', 24: 'Qd', 25: 'Kd', 26: 'Ah', 27: '2h', 28: '3h', 29: '4h', 30: '5h', 31: '6h',
           32: '7h', 33: '8h', 34: '9h', 35: 'Th', 36: 'Jh', 37: 'Qh', 38: 'Kh', 39: 'As', 40: '2s',
           41: '3s', 42: '4s', 43: '5s', 44: '6s', 45: '7s', 46: '8s', 47: '9s', 48: 'Ts', 49: 'Js', 50: 'Qs', 51: 'Ks'}
    dicB = {'Ac': 0, '2c': 1, '3c': 2, '4c': 3, '5c': 4, '6c': 5, '7c': 6, '8c': 7, '9c': 8, 'Tc': 9, 'Jc': 10, 'Qc': 11,
           'Kc': 12, 'Ad': 13, '2d': 14, '3d': 15, '4d': 16, '5d': 17, '6d': 18, '7d': 19, '8d': 20, '9d': 21, 'Td': 22,
           'Jd': 23, 'Qd': 24, 'Kd': 25, 'Ah': 26, '2h': 27, '3h': 28, '4h': 29, '5h': 30, '6h': 31, '7h': 32, '8h': 33,
           '9h': 34, 'Th': 35, 'Jh': 36, 'Qh': 37, 'Kh': 38, 'As': 39, '2s': 40, '3s': 41, '4s': 42, '5s': 43, '6s': 44,
           '7s': 45, '8s': 46, '9s': 47, 'Ts': 48, 'Js': 49, 'Qs': 50, 'Ks': 51}
    return sorted([dic[item] for item in cards], key=lambda x: dicB[x])


import codewars_test as test

@test.describe("Sample tests")
def sample_tests():
    @test.it("Encode")
    def it_1():
        test.assert_equals(encode(["Td", "8c", "Ks"]), [7, 22, 51])
        test.assert_equals(encode(["Qh", "5h", "Ad"]), [13, 30, 37])
        test.assert_equals(encode(["8c", "Ks", "Td"]), [7, 22, 51])
        test.assert_equals(encode(["Qh", "Ad", "5h"]), [13, 30, 37])

    @test.it("Decode")
    def it_2():
        test.assert_equals(decode([7, 22, 51]), ["8c", "Td", "Ks"])
        test.assert_equals(decode([13, 30, 37]), ["Ad", "5h", "Qh"])
        test.assert_equals(decode([7, 51, 22]), ["8c", "Td", "Ks"])
        test.assert_equals(decode([13, 37, 30]), ["Ad", "5h", "Qh"])
