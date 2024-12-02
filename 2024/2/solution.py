from utils.utils import *

def part1(input_data: list[str]) -> int:
    print('-----Part1-----')
    count: int = 0
    for report in input_data:
        if check_safety(report):
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

def part2(input_data: list[str]) -> int:
    print('-----Part2-----')
    ans = 0
    return ans

def main() -> None:
    print('-----DayN-----')
    input_data = get_data('input.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()