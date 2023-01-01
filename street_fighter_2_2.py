# https://www.codewars.com/kata/58583922c1d5b415b00000ff
# 5 kyu
import codewars_test as test
from copy import deepcopy


def super_street_fighter_selection(fighters, position, moves):
    def step_up(curr_pos):
        if table[curr_pos[0] - 1][curr_pos[1]] != '':
            curr_pos[0] -= 1
        return table[curr_pos[0]][curr_pos[1]]

    def step_down(curr_pos):
        if table[curr_pos[0] + 1][curr_pos[1]] != '':
            curr_pos[0] += 1
        return table[curr_pos[0]][curr_pos[1]]

    def step_left(curr_pos):
        curr_pos[1] = (curr_pos[1] - 1) % len(table[0])
        if table[curr_pos[0]][curr_pos[1]] == '':
            return step_left(curr_pos)
        else:
            return table[curr_pos[0]][curr_pos[1]]

    def step_right(curr_pos):
        curr_pos[1] = (curr_pos[1] + 1) % len(table[0])
        if table[curr_pos[0]][curr_pos[1]] == '':
            return step_right(curr_pos)
        else:
            return table[curr_pos[0]][curr_pos[1]]

    steps = {"up": step_up, "down": step_down, "left": step_left, "right": step_right}
    result = []
    table = deepcopy(fighters)
    l = len(fighters[0]) + 2
    for i, item in enumerate(table):
        table[i].insert(0, '')
        table[i].append('')
    table.insert(0, [''] * l)
    table.append([''] * l)
    pos = [position[0] + 1, position[1] + 1]
    for item in moves:
        result.append(steps[item](pos))
    return result


opts = ["up", "down", "right", "left"]

# DO NOT CHANGE THIS VARIABLE!
fighters = [
    ["", "Ryu", "E.Honda", "Blanka", "Guile", ""],
    ["Balrog", "Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat"],
    ["Vega", "T.Hawk", "Fei Long", "Deejay", "Cammy", "M.Bison"]
]


def copy(x):
    return [r[:] for r in x]


@test.describe("Character selection")
def _():
    @test.it("should work with no selection cursor moves")
    def _():
        moves = []
        position = (0, 0)
        solution = []
        test.assert_equals(super_street_fighter_selection(copy(fighters), position, moves), solution)

    @test.it("should stop on empty spaces vertically")
    def _():
        moves = ["up"]
        position = (1, 0)
        solution = ['Balrog']
        test.assert_equals(super_street_fighter_selection(copy(fighters), position, moves), solution)

    @test.it("should stop on empty spaces vertically")
    def _():
        moves = ["up"] * 4
        position = (1, 0)
        solution = ['Balrog'] * 4
        test.assert_equals(super_street_fighter_selection(copy(fighters), position, moves), solution)

    @test.it("should stop vertically")
    def _():
        moves = ["down"] * 4
        position = (1, 0)
        solution = ['Vega'] * 4
        test.assert_equals(super_street_fighter_selection(copy(fighters), position, moves), solution)

    @test.it("should stop on empty spaces vertically")
    def _():
        moves = ["up"] * 4
        position = (1, 5)
        solution = ['Sagat'] * 4
        test.assert_equals(super_street_fighter_selection(copy(fighters), position, moves), solution)

    @test.it("should stop vertically")
    def _():
        moves = ["down"] * 4
        position = (1, 5)
        solution = ['M.Bison'] * 4
        test.assert_equals(super_street_fighter_selection(copy(fighters), position, moves), solution)

    @test.it("should rotate horizontally")
    def _():
        moves = ["left"] * 8
        position = (1, 3)
        solution = ['Chun Li', 'Ken', 'Balrog', 'Sagat', 'Dhalsim', 'Zangief', 'Chun Li', 'Ken']
        test.assert_equals(super_street_fighter_selection(copy(fighters), position, moves), solution)

    @test.it("should rotate horizontally with empty spaces")
    def _():
        moves = ["right"] * 8
        position = (0, 2)
        solution = ['Blanka', 'Guile', 'Ryu', 'E.Honda', 'Blanka', 'Guile', 'Ryu', 'E.Honda']
        test.assert_equals(super_street_fighter_selection(copy(fighters), position, moves), solution)

    @test.it("should rotate on all rows")
    def _():
        moves = ["right"] * 6 + ["down"] + ["left"] * 12 + ["down"] + ["right"] * 12
        position = (0, 2)
        solution = ['Blanka', 'Guile', 'Ryu', 'E.Honda', 'Blanka', 'Guile', 'Dhalsim', 'Zangief', 'Chun Li', 'Ken',
                    'Balrog', 'Sagat', 'Dhalsim', 'Zangief', 'Chun Li', 'Ken', 'Balrog', 'Sagat', 'Dhalsim', 'Cammy',
                    'M.Bison', 'Vega', 'T.Hawk', 'Fei Long', 'Deejay', 'Cammy', 'M.Bison', 'Vega', 'T.Hawk', 'Fei Long',
                    'Deejay', 'Cammy']
        test.assert_equals(super_street_fighter_selection(copy(fighters), position, moves), solution)

    # DO NOT CHANGE THIS VARIABLE!
    # LIST WITH HOLES AND DUPLICATES
    fighters3 = [
        ["", "Ryu", "E.Honda", "Cammy", "Blanka", "Guile", "", "Chun Li"],
        ["Balrog", "Ken", "Chun Li", "", "M.Bison", "Zangief", "Dhalsim", "Sagat"],
        ["Vega", "", "Fei Long", "Balrog", "Deejay", "Cammy", "", "T.Hawk"]
    ]

    @test.it("should rotate on all rows")
    def _():
        moves = ["right"] * 6 + ["down"] + ["left"] * 12 + ["down"] + ["right"] * 12
        position = (0, 2)
        solution = ['Cammy', 'Blanka', 'Guile', 'Chun Li', 'Ryu', 'E.Honda', 'Chun Li', 'Ken', 'Balrog', 'Sagat',
                    'Dhalsim', 'Zangief', 'M.Bison', 'Chun Li', 'Ken', 'Balrog', 'Sagat', 'Dhalsim', 'Zangief', 'Cammy',
                    'T.Hawk', 'Vega', 'Fei Long', 'Balrog', 'Deejay', 'Cammy', 'T.Hawk', 'Vega', 'Fei Long', 'Balrog',
                    'Deejay', 'Cammy']
        test.assert_equals(super_street_fighter_selection(copy(fighters3), position, moves), solution)

    @test.it("should work")
    def _():
        moves = ["down"] + ["right"] * 3 + ["down"] + ["left"] * 2 + ["down"] + ["right"] * 3 + ["up"]
        position = (0, 3)
        solution = ['Cammy', 'Blanka', 'Guile', 'Chun Li', 'Sagat', 'Dhalsim', 'Zangief', 'Cammy', 'T.Hawk', 'Vega',
                    'Fei Long', 'Chun Li']
        test.assert_equals(super_street_fighter_selection(copy(fighters3), position, moves), solution)

    fighters4 = [
        ["", "Ryu", "E.Honda", "Cammy"],
        ["Balrog", "Ken", "Chun Li", ""],
        ["Vega", "", "Fei Long", "Balrog", ],
        ["Blanka", "Guile", "", "Chun Li"],
        ["M.Bison", "Zangief", "Dhalsim", "Sagat"],
        ["Deejay", "Cammy", "", "T.Hawk"]
    ]

    @test.it("should work with longer grid")
    def _():
        moves = ["left"] * 2 + ["down"] + ["right"] * 4 + ["down"] + ["left"] * 4 + ["down"] + ["right"] * 2 + [
            "down"] + ["right"] * 3 + ["down"] + ["left"] * 3 + ["down"] + ["left"] * 3
        position = (0, 3)
        solution = ['E.Honda', 'Ryu', 'Ken', 'Chun Li', 'Balrog', 'Ken', 'Chun Li', 'Fei Long', 'Vega', 'Balrog',
                    'Fei Long', 'Vega', 'Blanka', 'Guile', 'Chun Li', 'Sagat', 'M.Bison', 'Zangief', 'Dhalsim',
                    'Dhalsim', 'Zangief', 'M.Bison', 'Sagat', 'T.Hawk', 'Cammy', 'Deejay', 'T.Hawk']
        test.assert_equals(super_street_fighter_selection(copy(fighters4), position, moves), solution)

    @test.it("should work with odd initial position")
    def _():
        moves = ["left"] * 2 + ["down"] + ["right"] * 4 + ["down"] + ["left"] * 4 + ["up"] + ["right"] * 2 + ["up"] + [
            "right"] * 3
        position = (3, 3)
        solution = ['Guile', 'Blanka', 'M.Bison', 'Zangief', 'Dhalsim', 'Sagat', 'M.Bison', 'Deejay', 'T.Hawk', 'Cammy',
                    'Deejay', 'T.Hawk', 'Sagat', 'M.Bison', 'Zangief', 'Guile', 'Chun Li', 'Blanka', 'Guile']
        test.assert_equals(super_street_fighter_selection(copy(fighters4), position, moves), solution)
