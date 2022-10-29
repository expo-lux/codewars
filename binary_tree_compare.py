# https://www.codewars.com/kata/55847fcd3e7dadc9f800005f
import codewars_test as test


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


# best solution
# def compare(a, b):
#     return a.val == b.val and compare(a.left, b.left) and compare(a.right, b.right) if a and b else a == b

def compare(a, b) -> bool:
    if a is not None and b is not None:  # if a and b:
        if a.val != b.val:
            return False
        else:  # left compare
            if a.left is not None and b.left is not None:
                res_left = compare(a.left, b.left)
            elif a.left == b.left:
                res_left = True
            else:
                res_left = False
            if a.right is not None and b.right is not None:
                res_right = compare(a.right, b.right)
            elif a.right == b.right:
                res_right = True
            else:
                res_right = False
            return res_left and res_right
    # else return a == b
    elif a == b:
        return True
    else:
        return False


a_node = Node(1, None, None)
b_node = Node(1, None, None)
c_node = Node(2, None, None)

test.describe("example tests")

results1 = compare(a_node, b_node);
test.it("Should return true for equal nodes")
test.assert_equals(results1, True)

results2 = compare(a_node, c_node);
test.it("Should return false for non-equal nodes")
test.assert_equals(results2, False)
