from utils.utils import *

def part1(input_data: list[str]) -> int:
    print('-----Part1-----')
    n_matches = 0
    total = 0
    for line in input_data:
        winning_nums = list(filter(''.__ne__, line.split(':')[1].split('|')[0].split(' ')))
        your_nums = list(filter(''.__ne__, line.split(':')[1].split('|')[1].split(' ')))
        all_nums = winning_nums + your_nums
        a = len(all_nums)
        b = len(list(set(all_nums)))
        n_matches = a - b
        if n_matches > 0:
            total += pow(2, n_matches - 1)
    return total

def part2(input_data: list[str]) -> int:
    print('-----Part2-----')
    return 0

def main() -> None:
    print('-----DayN-----')
    input_data = get_data('test.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()