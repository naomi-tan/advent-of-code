from utils import utils
from utils import TreeUtils

def part1(input_data: list[list[int]]) -> int:
    print('-----Part1-----')
    ans: int = 0

    # find all 0s
    zeros = []
    row = 0
    for line in input_data:
        print(line)
        col = 0
        for char in line:
            if char == 0:
                zeros.append([row, col])
            col += 1
        row += 1
    tree_conversion(input_data, zeros)


    # # get neighbours
    # for i in range(len(zeros)):
    #     # neighbours = utils.get_manhattan_neighbours(input_data, zeros[i])

    # bfs or dfs needed
    # convert data to tree of +1 values
    # if +1 add to possible routes
    # if no neighbours and last is not 9 delete from poss route list
    # if end add count for 0 index
    return ans

class Data:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col

def tree_conversion(input_data: list[list[int]], start_nodes: list[list[int]]) -> list[list[int]]:
    tree = []
    max_depth = 9
    for i in range(len(start_nodes)):
        tree.append(TreeUtils.Node(Data(input_data[start_nodes[i][0]][start_nodes[i][1]],start_nodes[i][0],start_nodes[i][1])))
    print(tree[0].data.col)

def part2(input_data: list[list[int]]) -> int:
    print('-----Part2-----')
    ans: int = 0
    return ans

def main() -> None:
    print('-----DayN-----')
    input_data: list[list[int]] = list(map(lambda a: list(map(lambda b: int(b), a)), utils.read_char_arr('test.txt')))
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()