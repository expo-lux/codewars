# https://www.codewars.com/kata/5268988a1034287628000156
import codewars_test as test
from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return self.data


def serpentine_traversal(root_node: Node) -> list:
    dic = {}
    q = deque()
    q.append((root_node, 1))
    while q:
        node, depth = q.popleft()
        if node:
            if node.data is not None:
                dic.setdefault(depth, []).append(node.data)
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
    res = []
    for k, v in dic.items():
        if k % 2 == 0:
            v.reverse()
            res.extend(v)
        else:
            res.extend(v)
    return res


@test.describe("sample tests")
def sample_tests():
    def do_test(tree, expected):
        actual = serpentine_traversal(tree)
        test.assert_equals(actual, expected)

    @test.it("empty tree")
    def empty_tree():
        do_test(None, [])

    @test.it("example from description")
    def example_from_description():
        tree = (
            Node('A',
                 Node('B',
                      Node('D'),
                      Node('E')
                      ),
                 Node('C',
                      Node('F'),
                      Node('G')
                      )
                 )
        )
        do_test(tree, ["A", "C", "B", "D", "E", "F", "G"])

    @test.it("unbalanced tree")
    def unbalanced_tree():
        tree = (
            Node('A',
                 None,
                 Node('B',
                      Node('C',
                           None,
                           Node('F',
                                Node('G',
                                     Node('H')
                                     )
                                )
                           ),
                      Node('D',
                           None,
                           Node('E')
                           )
                      )
                 )
        )
        do_test(tree, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
