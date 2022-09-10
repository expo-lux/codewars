import re


def increment_string(strng):
    res = re.findall('\d+$', strng)
    if res:
        repl = str(int(res[0]) + 1).zfill(len(res[0]))
        return strng.replace(res[0], repl)
    else:
        return strng + '1'


assert increment_string("foo") == "foo1", "Error"
assert increment_string("foobar001") == "foobar002", "Error"
assert increment_string("foobar1") == "foobar2", "Error"
assert increment_string("foobar00") == "foobar01", "Error"
assert increment_string("foobar99") == "foobar100", "Error"
assert increment_string("foobar099") == "foobar100", "Error"
assert increment_string("") == "1", "Error"
assert increment_string(
    "xR982659RNV=m%J7}$0584443w_SW7378435zr5(a21598936H#_Ej5555s>l4566595900000042349") == "xR982659RNV=m%J7}$0584443w_SW7378435zr5(a21598936H#_Ej5555s>l4566595900000042350", "Error"
