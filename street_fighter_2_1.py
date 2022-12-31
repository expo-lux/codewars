# https://www.codewars.com/kata/5853213063adbd1b9b0000be
# 6 kyu
import codewars_test as test


def street_fighter_selection(fighters, initial_position, moves):
    move = {"up": [0, -1], "down": [0, 1], "left": [-1, 0], "right": [1, 0]}
    pos = [initial_position[1], initial_position[0]]
    Xmax_index = len(fighters[0]) - 1
    results = []
    for item in moves:
        pos[0] += move[item][0]
        pos[1] += move[item][1]
        if pos[1] < 0:
            pos[1] = 0
        if pos[1] > 1:
            pos[1] = 1
        if pos[0] < 0:
            pos[0] = Xmax_index
        if pos[0] > Xmax_index:
            pos[0] = 0
        results.append(fighters[pos[1]][pos[0]])
    return results


fighters = [
    ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
    ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
opts = ["up", "down", "right", "left"]


@test.describe("Fixed tests")
def _():
    @test.it("random")
    def _():
        moves = ['right', 'right', 'right']
        solution = ['Ken', 'Chun Li', 'Zangief']
        test.assert_equals(street_fighter_selection(fighters, (1, 5), moves), solution)

    @test.it("should work with no selection cursor moves")
    def _():
        moves = []
        solution = []
        test.assert_equals(street_fighter_selection(fighters, (0, 0), moves), solution)

    @test.it("should go left 8 times")
    def _():
        moves = ["left"] * 8
        solution = ['Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega', 'Balrog']
        test.assert_equals(street_fighter_selection(fighters, (0, 0), moves), solution)

    @test.it("should go right 8 times")
    def _():
        moves = ["right"] * 8
        solution = ['E.Honda', 'Blanka', 'Guile', 'Balrog', 'Vega', 'Ryu', 'E.Honda', 'Blanka']
        test.assert_equals(street_fighter_selection(fighters, (0, 0), moves), solution)

    @test.it("should go up 4 times, always the same")
    def _():
        moves = ["up"] * 4
        solution = ['Ryu', 'Ryu', 'Ryu', 'Ryu']
        test.assert_equals(street_fighter_selection(fighters, (0, 0), moves), solution)

    @test.it("should go down 4 times, always the same")
    def _():
        moves = ["down"] * 4
        solution = ['Ken', 'Ken', 'Ken', 'Ken']
        test.assert_equals(street_fighter_selection(fighters, (0, 0), moves), solution)

    @test.it("should use all 4 directions counter-clockwise twice")
    def _():
        moves = ["down", "right", "up", "left"] * 2
        solution = ['Ken', 'Chun Li', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'E.Honda', 'Ryu']
        test.assert_equals(street_fighter_selection(fighters, (0, 0), moves), solution)

    @test.it("should use all 4 directions clockwise twice")
    def _():
        moves = ["up", "left", "down", "right"] * 2
        solution = ['Ryu', 'Vega', 'M.Bison', 'Ken', 'Ryu', 'Vega', 'M.Bison', 'Ken']
        test.assert_equals(street_fighter_selection(fighters, (0, 0), moves), solution)
