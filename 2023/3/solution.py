from utils.utils import *
import math

class Part:
    def __init__(self, value: int, row: int, col: int, length: int, typeof: str):
        self.value = value
        self.row = row
        self.col = col
        self.length = length
        self.typeof = typeof

def number_search(row: str, pos: int) -> int:
    arr = list(row)

def part1(input_data: list[str], char_arr: list[list[str]]) -> int:
    print('-----Part1-----')
    line_num: int = 0
    # find all numbers
    iterator = re.compile(r'\d+')
    total = 0
    for line in input_data:
        for i in iterator.finditer(line):
            part: Part = Part(int(i.group()), line_num, i.start(), len(str(i.group())), 'number')
            # get neighbours of numbers
            neighbours: list[str] = get_neighbours(char_arr, part.row, part.col, part.length)
            # check if number is next to symbol
            neighbours: list[str] = list(filter('.'.__ne__, neighbours))
            neighbours: list[str] = list(filter(''.__ne__, neighbours))
            if len(neighbours) > 0:
                total += int(part.value)
        line_num += 1
    return total

def part2(input_data: list[str], char_arr: list[list[str]]) -> int:
    print('-----Part2-----')
    # find all * next ot exactly 2 numbers
    # gear ratio is 2 nums multiplied together
    # sum of gear ratios

    # check digits aren't part of same number

    # find all *
    iterator = re.compile(r'\*')
    line_num = 0
    offset = [-1, 0, 1, -1, 1, -1, 0, 1]
    for line in input_data:
        print(line)
        for i in iterator.finditer(line):
            # check numbers distance to point 1 from each digit, if less than 2 add to array
            # check surrounding lines for numbers
            for j in range(3):
                nums = find_nums(input_data[line_num + j - 1])
                for num in nums:
                    k = 0
                    chars = list(str(num))
                    for char in chars:
                        dist = math.dist((num.start() + k, line_num + j - 1), (i.start() , line_num))
                        if dist < 2:
                            print(num.group(), dist, num.start() + k, line_num + j - 1, i.start(), line_num)
                        k += 1
            # # get neighbours of *
            # neighbours = get_neighbours(char_arr, line_num, i.start(), 1)
            # # * * *
            # # * N *
            # # * * *
            # j = 0
            # n1 = neighbours[0:3]
            # n2 = neighbours[3:5]
            # n3 = neighbours[5:8]
            # print(neighbours, n1, n2, n3)
            # for neighbour in neighbours:
            #     if neighbour.isdigit():
            #         number_search(line, i.start() + offset[j])
            #     j += 1
        line_num += 1
    return 0

def main() -> None:
    print('-----DayN-----')
    input_data = get_data('test.txt')
    char_arr = raw_to_char_arr(input_data)
    print(part1(input_data, char_arr))
    print(part2(input_data, char_arr))

if __name__ == '__main__':
    main()