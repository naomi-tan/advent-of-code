from utils.utils import *
import numpy as np

def part1(input_data: list[str]) -> int:
    print('-----Part1-----')
    count: int = 0
    for report in input_data:
        # split report into numbers
        values: object = np.array(list(map(lambda a: int(a), report.split())))
        if check_safety(values):
            count += 1
    return count

def part2(input_data: list[str]) -> int:
    print('-----Part2-----')
    count: int = 0
    for report in input_data:
        # split report into numbers
        values: object = np.array(list(map(lambda a: int(a), report.split())))
        if check_safety(values):
            count += 1
        else:
            # more efficient if just remove 2 that cause problem
            for i in range(values.size):
                removed_vals = np.delete(values, i)
                if check_safety(removed_vals):
                    count += 1
                    break
    return count

def check_safety(values: object) -> bool:
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

def main() -> None:
    print('-----DayN-----')
    input_data = get_data('input.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()