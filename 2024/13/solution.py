from utils import utils

def part1(input_data: str) -> int:
    print('-----Part1-----')
    ans: int = 0
    # simultaneous equations
    # solve graphically
    # point of intersection of 2 lines

    # define constants
    A_PRICE = 3
    B_PRICE = 1

    # parse data
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
                prize_positions.append([int(nums[0].group()), int(nums[1].group())])

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
        x = (b1*c2 - b2*c1) / (a1*b2 - a2*b1)
        y = (c1*a2 - c2*a1) / (a1*b2 - a2*b1)
        if (0 <= x <= 100) and (0 <= y <= 100) and (x - int(x) == 0) and (y - int(y) == 0):
            ans += int(x)*A_PRICE + int(y)*B_PRICE
    return ans

def part2(input_data: str) -> int:
    print('-----Part2-----')
    ans: int = 0
    error = 10000000000000

    # define constants
    A_PRICE = 3
    B_PRICE = 1

    # parse data
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
        if (0 <= x) and (0 <= y) and (x - int(x) == 0) and (y - int(y) == 0):
            ans += int(x) * A_PRICE + int(y) * B_PRICE
    return ans

def main() -> None:
    print('-----DayN-----')
    input_data: str = utils.read_str('input.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()