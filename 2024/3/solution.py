from utils.utils import *
import re
import math

def part1(input_data: str) -> int:
    print('-----Part1-----')
    # find all valid instructions
    ins: list[str] = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', input_data)

    # get result of instructions and sum
    ans: int = 0
    for i in ins:
        digits: list[int] = list(map(lambda a: int(a), re.findall('[0-9]{1,3}', i)))
        ans += digits[0] * digits[1]
    return ans

def part2(input_data: str) -> int:
    print('-----Part2-----')
    # find all valid instructions
    mul: iter = re.finditer(r'mul\([0-9]{1,3},[0-9]{1,3}\)', input_data)
    do: iter = re.finditer(r'do\(\)', input_data)
    dont: iter = re.finditer(r'don\'t\(\)', input_data)

    enabled: bool = True
    d = next(do).start()
    n = next(dont).start()
    ans = 0
    for m in mul:
        # check if previous instruction is do()
        if d < m.start():
            enabled = True
            try:
                # get position of next do() instruction
                d = next(do).start()
            except StopIteration:
                d = math.inf
        # check if previous instruction is don't()
        if n < m.start():
            enabled = False
            try:
                # get position of next don't() instruction
                n = next(dont).start()
            except StopIteration:
                n = math.inf
        # only add if previous instruction was do()
        if enabled:
            digits: list[int] = list(map(lambda a: int(a), re.findall(r'[0-9]{1,3}', m.group())))
            ans += digits[0] * digits[1]
    return ans

def main() -> None:
    print('-----DayN-----')
    input_data = get_raw('input.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()