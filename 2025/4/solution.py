from utils import utils
import copy

def get_rolls(input_data: list[list[str]]) -> {int, list[list[str]]}:
    rolls: int = 0
    output_data = copy.deepcopy(input_data)
    for i in range(len(input_data)):
        for j in range(len(input_data[0])):
            if input_data[i][j] == '@':
                neighbours = utils.get_neighbours(input_data, i, j)
                count = sum([(1 if n=='@' else 0) for n in neighbours])
                if count < 4:
                    rolls += 1
                    output_data[i][j] = 'x'
    return rolls, output_data

def part1(input_data: list[list[str]]) -> int:
    print('-----Part1-----')
    ans: int = 0
    rolls, output_data = get_rolls(input_data)
    ans = rolls
    return ans

def part2(input_data: list[list[str]]) -> int:
    print('-----Part2-----')
    ans: int = 0
    rolls = 1
    while rolls > 0:
        rolls, output_data = get_rolls(input_data)
        ans += rolls
        input_data = copy.deepcopy(output_data)
    return ans

def main() -> None:
    print('-----DayN-----')
    input_data: list[list[str]] = utils.read_char_arr('input.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()