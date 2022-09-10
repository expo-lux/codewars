import codewars_test as test
import string


class MixItem:
    def __init__(self, s_id: str, char: str, count: int):
        self.string_id = s_id
        self.count = count
        self.char = char

    def __repr__(self):
        return f"{self.string_id}:{self.char * self.count}"

    def __lt__(self, other):
        if not isinstance(other, MixItem):
            raise TypeError("Invalid type")
        return self.count > other.count or \
               self.count == other.count and (self.string_id, self.char) < (other.string_id, other.char)


def mix(s1, s2):
    res, res_string = [], ''
    for i in string.ascii_lowercase:
        x1, x2 = s1.count(i), s2.count(i)
        if max(x1, x2) <= 1:
            continue
        else:
            if x1 > x2:
                item = MixItem('1', i, x1)
            elif x1 < x2:
                item = MixItem('2', i, x2)
            else:
                item = MixItem('=', i, x1)
            res.append(item)
    res.sort()
    res = list(map(str, res))
    return "/".join(res)


test.assert_equals(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
test.assert_equals(mix("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp"),
                   '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
test.assert_equals(mix("looping is fun but dangerous", "less dangerous than coding"),
                   "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
test.assert_equals(mix(" In many languages", " there's a pair of functions"),
                   "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
test.assert_equals(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
test.assert_equals(mix("codewars", "codewars"), "")
test.assert_equals(mix("A generation must confront the looming ", "codewarrs"),
                   "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")
