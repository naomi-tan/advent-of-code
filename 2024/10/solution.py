from utils import utils
from utils import TreeUtils

def part1(input_data: list[list[int]]) -> int:
    print('-----Part1-----')
    ans: int = 0

    # find all 0s
    zeros = []
    row = 0
    for line in input_data:
        col = 0
        for char in line:
            if char == 0:
                zeros.append([row, col])
            col += 1
        row += 1

    for i in range(len(zeros)):
        [root, all_ends] = create_tree(input_data, zeros[i])
        total_summits = 0
        for end in set(all_ends):
            if end[0] == 9:
                total_summits += 1
        ans += total_summits
    return ans

class Data:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col

def create_tree(input_data: list[list[int]], root_node: list[int]) -> TreeUtils.Node:
    # data = Data(input_data[root_node[0]][root_node[1]], root_node[0], root_node[1])
    data = tuple([input_data[root_node[0]][root_node[1]], root_node[0], root_node[1]])
    root = TreeUtils.Node(data)
    neighbour_pos = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    parent_nodes = [root]
    i = 0
    all_ends = []
    while True:
        child_nodes = []
        for node in parent_nodes:
            neighbours = utils.get_manhattan_neighbours(input_data, [node.data[1], node.data[2]])
            for j in range(4):
                if neighbours[j] == node.data[0] + 1:
                    # data = Data(neighbours[j], node.data[1] + neighbour_pos[j][0], node.data[2] + neighbour_pos[j][1])
                    data = tuple([neighbours[j], node.data[1] + neighbour_pos[j][0], node.data[2] + neighbour_pos[j][1]])
                    child = TreeUtils.Node(data)
                    node.add_child(child)
                    child_nodes.append(child)
                    all_ends.append(child.data)
        parent_nodes = child_nodes
        if len(child_nodes) == 0:
            break
        i += 1
    total_summits = 0
    return [root, all_ends]


def part2(input_data: list[list[int]]) -> int:
    print('-----Part2-----')
    ans: int = 0

    # find all 0s
    zeros = []
    row = 0
    for line in input_data:
        col = 0
        for char in line:
            if char == 0:
                zeros.append([row, col])
            col += 1
        row += 1

    for i in range(len(zeros)):
        [root, all_ends] = create_tree(input_data, zeros[i])
        total_summits = 0
        for end in all_ends:
            if end[0] == 9:
                total_summits += 1
        ans += total_summits
    return ans

def main() -> None:
    print('-----DayN-----')
    input_data: list[list[int]] = list(map(lambda a: list(map(lambda b: int(b), a)), utils.read_char_arr('input.txt')))
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()