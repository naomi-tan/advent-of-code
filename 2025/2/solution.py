from utils import utils
import re

def part1(input_data: list[str]) -> int:
    print('-----Part1-----')
    ans: int = 0
    # split input data into id ranges
    id_ranges: [] = [[int(x) for x in item.split('-')] for item in input_data]
    # get all invalid ID's in range
    for [start, end] in id_ranges:
        # get all possible lengths of numbers in range
        for i in range(len(str(start)), len(str(end)) + 1):
            # check if valid length i.e. divisible by 2
            if i%2 == 0:
                # get first repeating number of length
                x = int(str(start)[:int(i/2)]) if len(str(start)) == i else int('1' + ''.join(['0']*(int(i/2)-1)))
                n = int(str(x)*2)
                while n <= end:
                    if n >= start:
                        ans += n
                    x += 1
                    n = int(str(x)*2)
    print(ans)
    return ans

def part2(input_data: list[str]) -> int:
    print('-----Part2-----')
    ans: int = 0
    # split input data into id ranges
    id_ranges: [] = [[int(x) for x in item.split('-')] for item in input_data]
    # get all invalid ID's in range
    for [start, end] in id_ranges:
        print(start, end)
    print(ans)
    return ans

def main() -> None:
    print('-----DayN-----')
    input_data: list[str] = utils.read_csv('input.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()