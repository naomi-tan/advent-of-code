from utils import utils
import numpy as np

# define constants
A_PRICE = 3
B_PRICE = 1

def part1(input_data: str) -> int:
    print('-----Part1-----')
    ans: int = 0
    # simultaneous equations
    # solve graphically
    # point of intersection of 2 lines
    [a_translations, b_translations, prize_positions] = parse_data(input_data)
    ans = calculate_presses(a_translations, b_translations, prize_positions, 100)
    return ans

def part2(input_data: str) -> int:
    print('-----Part2-----')
    ans: int = 0
    [a_translations, b_translations, prize_positions] = parse_data(input_data, 10000000000000)
    ans = calculate_presses(a_translations, b_translations, prize_positions)
    return ans

def parse_data(input_data: str, error: int=0):
    input_data = input_data.split('\n\n')
    input_data = list(map(lambda a: a.split('\n'), input_data))
    a_translations = []
    b_translations = []
    prize_positions = []
    for machine in input_data:
        for line in machine:
            nums = utils.find_nums(line)
            if line.find('Button A') != -1:
                a_translations.append([int(nums[0].group()), int(nums[1].group())])
            if line.find('Button B') != -1:
                b_translations.append([int(nums[0].group()), int(nums[1].group())])
            if line.find('Prize') != -1:
                prize_positions.append([int(nums[0].group()) + error, int(nums[1].group()) + error])
    return [a_translations, b_translations, prize_positions]

def calculate_presses(a_translations, b_translations, prize_positions, upper_lim=np.inf):
    cost = 0
    # for each machine find intersection of lines
    for a, b, p in zip(a_translations, b_translations, prize_positions):
        # line 1
        a1 = a[0]
        b1 = b[0]
        c1 = -(p[0])
        # line 2
        a2 = a[1]
        b2 = b[1]
        c2 = -(p[1])
        # intersection
        x = (b1 * c2 - b2 * c1) / (a1 * b2 - a2 * b1)
        y = (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)
        if (0 <= x <= upper_lim) and (0 <= y <= upper_lim) and (x - int(x) == 0) and (y - int(y) == 0):
            # calculate cost
            cost += int(x) * A_PRICE + int(y) * B_PRICE
    return cost

def main() -> None:
    print('-----DayN-----')
    input_data: str = utils.read_str('input.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()