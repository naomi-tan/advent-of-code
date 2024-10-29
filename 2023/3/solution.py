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
    # find all *
    iterator = re.compile(r'\*')
    line_num = 0
    offset = [-1, 0, 1, -1, 1, -1, 0, 1]
    total = 0
    for line in input_data:
        for i in iterator.finditer(line):
            # check surrounding lines for numbers
            adj_nums = []
            for j in range(3):
                nums = find_nums(input_data[line_num + j - 1])
                for num in nums:
                    k = 0
                    chars = list(str(num.group()))
                    for char in chars:
                        # check numbers distance to point 1 from each digit, if less than 2 add to array
                        dist = math.dist((num.start() + k, line_num + j - 1), (i.start() , line_num))
                        # must be adjacent to exactly 2 part numbers
                        if dist < 2:
                            adj_nums.append(num.group())
                            break
                        k += 1
            if len(adj_nums) == 2:
                total += (int(adj_nums[0]) * int(adj_nums[1]))
        line_num += 1
    return total

def main() -> None:
    print('-----DayN-----')
    input_data = get_data('input.txt')
    char_arr = raw_to_char_arr(input_data)
    print(part1(input_data, char_arr))
    print(part2(input_data, char_arr))

if __name__ == '__main__':
    main()