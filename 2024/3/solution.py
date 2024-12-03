from utils.utils import *
import re

def part1(input_data: str) -> int:
    print('-----Part1-----')
    # find all valid instructions
    ins: list[str] = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', input_data)

    # get result of instructions and sum
    ans: int = 0
    for i in ins:
        digits: list[int] = list(map(lambda a: int(a), re.findall('[0-9]{1,3}', i)))
        ans += digits[0] * digits[1]
    return ans

def part2(input_data: str) -> int:
    print('-----Part2-----')
    ans = 0
    return ans

def main() -> None:
    print('-----DayN-----')
    input_data = get_raw('input.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()