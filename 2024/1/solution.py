from utils.utils import *

def part1(input_data: list[list[str]]) -> int:
    print('-----Part1-----')

    # split data into 2 columns
    col1: list[int] = []
    col2: list[int] = []
    for line in input_data:
        col1.append(int(line[0]))
        col2.append(int(line[1]))

    # sort columns ascending
    col1.sort()
    col2.sort()

    # distance between pairs
    distance = 0
    for i in range(len(col1)):
        distance += abs(col1[i] - col2[i])

    return distance

def part2(input_data: list[list[str]]) -> int:
    print('-----Part2-----')

    # split data into 2 columns
    col1: list[int] = []
    col2: list[int] = []
    for line in input_data:
        col1.append(int(line[0]))
        col2.append(int(line[1]))

    # sort columns ascending
    col1.sort()
    col2.sort()

    # list similarity
    similarity: int = 0
    while len(col1) > 0:
        app1: int = appearances(col1, col1[0])
        app2: int = appearances(col2, col1[0])
        similarity += app1 * col1[0] * app2
        col1 = col1[app1:]

    return similarity

def appearances(input_ls: list[int], n: int) -> int:
    n = len(list(filter(lambda a : a == n, input_ls)))
    return n


def main() -> None:
    print('-----DayN-----')
    input_data = get_arr('input.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()