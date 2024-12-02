from utils.utils import *
import numpy as np

def part1(input_data: list[str]) -> int:
    print('-----Part1-----')
    count: int = 0
    for report in input_data:
        if check_safety2(report):
            count += 1
    return count

def check_safety(report: str) -> bool:
    # split report into numbers
    values: list[int] = list(map(lambda a: int(a), report.split()))

    # init stop cases
    safe: bool = True
    i: int = 1

    # init vars
    prev_val: int = values[0]
    increasing: bool = values[1] > values[0]

    while safe and (i < len(values)):
        # check same
        curr_val = values[i]
        if values[i] == prev_val:
            safe = False

        # check change in diff
        curr_d = values[i] > prev_val
        if curr_d != increasing:
            safe = False

        # check abs change
        if abs(values[i] - prev_val) > 3:
            safe = False

        prev_val = curr_val
        i += 1

    return safe

def check_safety2(report: str) -> bool:
    # split report into numbers
    values: object = np.array(list(map(lambda a: int(a), report.split())))

    # shift numbers 1 position
    shift: object = np.insert(values, 0, [0])

    # find difference between values
    subtract: object = shift - np.insert(values, values.size, [0])
    diff: object = np.delete(subtract, [0, subtract.size - 1])

    inc: list[int] = list(filter(lambda a: a > 0, diff.tolist()))
    dec: list[int] = list(filter(lambda a: a < 0, diff.tolist()))

    # if all increasing or all decreasing
    if (len(inc) == diff.size) or (len(dec) == diff.size):
        # if 0 < absolute value < 4
        absolute: list[int] = list(filter(lambda a: 0 < abs(a) < 4, diff.tolist()))
        if len(absolute) == diff.size:
            return True
        else:
            return False
    else:
        return False


def part2(input_data: list[str]) -> int:
    print('-----Part2-----')
    ans = 0
    # if fails, remove number it fails on and test
    # if that fails remove other numbers
    # if all fails, not safe

    # shift all vals 1 space
    # subtract
    return ans

def main() -> None:
    print('-----DayN-----')
    input_data = get_data('input.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()