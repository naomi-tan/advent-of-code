from utils import utils
import math

def part1(input_data: list[str]) -> int:
    print('-----Part1-----')
    ans: int = 0
    location: int = 50
    # parse direction and distance
    instructions: list[list[str]] = [[line[0], int(line[1::])] for line in input_data]
    # execute each instruction
    for [direction, distance] in instructions:
        # %100 to ignore full rotations
        location += (-(distance%100) if direction == 'L' else distance%100)
        location += (100 if location < 0 else 0)
        location -= (100 if location > 99 else 0)
        ans += (1 if location == 0 else 0)
    return ans

def part2(input_data: list[str]) -> int:
    print('-----Part2-----')
    ans: int = 0
    location: int = 50
    prev_loc: int = 50
    # parse direction and distance
    instructions: list[list[str]] = [[line[0], int(line[1::])] for line in input_data]
    # execute each instruction
    for [direction, distance] in instructions:
        # add full rotations
        ans += math.floor(abs(distance)/100)
        # %100 to ignore full rotations
        location += (-(distance%100) if direction == 'L' else distance%100)
        ans += 1 if location == 0 else 0
        if location < 0:
            ans += 1 if prev_loc != 0 else 0
            location += 100
        if location > 99:
            ans += 1 if prev_loc != 0 else 0
            location -= 100
        prev_loc = location
    return ans

def main() -> None:
    print('-----Day1-----')
    input_data: list[str] = utils.read_lines('input.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()