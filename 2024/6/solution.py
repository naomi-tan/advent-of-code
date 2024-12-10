from utils import utils
import copy

def part1(input_data: list[list[str]]):
    print('-----Part1-----')
    ans = 0
    stop = False
    [direction, position] = init_pos(input_data)
    while not stop:
        [next_char, next_pos] = look_ahead(input_data, direction, position)
        if next_char == '#':
            direction = turn(direction)
            input_data[position[0]][position[1]] = direction
        elif next_char == '!':
            input_data[position[0]][position[1]] = 'x'
            stop = True
        else:
            step(input_data, position, direction, next_pos)
            position = next_pos
    for line in input_data:
        ans += line.count('x')
    return ans

def init_pos(input_data: list[list[str]]) -> list[str|list[int]]:
    direction = ''
    position = []
    row = 0
    for line in input_data:
        col = 0
        for char in line:
            if char == '^' or char == '>' or char == 'v' or char =='<':
                direction = char
                position = [row, col]
            col += 1
        row += 1
    return [direction, position]

def look_ahead(input_data: list[list[str]], direction: str, position: list[int]) -> list[str|list[int]]:
    if direction == '^':
        next_pos = [position[0] - 1, position[1]]
    elif direction == '>':
        next_pos = [position[0], position[1] + 1]
    elif direction == 'v':
        next_pos = [position[0] + 1, position[1]]
    else: # direction == '<':
        next_pos = [position[0], position[1] - 1]
    if ( 0 <= next_pos[0] < len(input_data)) and (0 <= next_pos[1] < len(input_data[0])):
        next_char = input_data[next_pos[0]][next_pos[1]]
    else:
        next_char = '!'
    return [next_char, next_pos]

def step(input_data: list[list[str]], position: list[int], direction: str, next_pos: list[int]) -> None:
    input_data[position[0]][position[1]] = 'x'
    input_data[next_pos[0]][next_pos[1]] = direction

def turn(direction: str):
    directions: list[str] = ['^', '>', 'v', '<']
    i = directions.index(direction) + 1
    try:
        new_dir = directions[i]
    except IndexError:
        new_dir = directions[0]
    return new_dir

def part2(input_data2: list[list[str]], route: list[list[int]]):
    print('-----Part2-----')
    ans = 0
    # for each step in route, check for loop or exit map, count no of loops
    for stepped_pos in route:
        input_data = copy.deepcopy(input_data2)
        [direction, position] = init_pos(input_data)
        if position != stepped_pos:
            # don't put obstacle directly on guard
            input_data[stepped_pos[0]][stepped_pos[1]] = '#'
        exit_map = False
        loop = False
        i = 0
        dir_map = {}
        # drop_dir(dir_map, position, direction)
        while not exit_map and not loop and (i < 10000):
            [next_char, next_pos] = look_ahead(input_data, direction, position)
            if next_char == '#':
                loop = drop_dir(dir_map, position, direction)
                direction = turn(direction)
                input_data[position[0]][position[1]] = direction
            elif next_char == '!':
                input_data[position[0]][position[1]] = 'x'
                exit_map = True
            else:
                loop = drop_dir(dir_map, position, direction)
                step(input_data, position, direction, next_pos)
                position = next_pos
            i += 1
        if loop:
            ans += 1
    return ans

def drop_dir(dir_map: dict, position: list[int], direction: str) -> bool:
    dir_key = ','.join(list(map(lambda a: str(a), position)))
    if dir_key in dir_map:
        if direction in dir_map[dir_key]:
            # loop found
            return True
        else:
            dir_map[dir_key].append(direction)
            return False
    else:
        dir_map[dir_key] = [direction]
        return False

def main() -> None:
    print('-----DayN-----')
    char_arr1: list[list[str]] = utils.read_char_arr('input.txt')
    char_arr2: list[list[str]] = utils.read_char_arr('input.txt')
    print(part1(char_arr1))
    route = []
    for row in range(len(char_arr1)):
        for col in range(len(char_arr1[0])):
            if char_arr1[row][col] == 'x':
                route.append([row, col])
    print(part2(char_arr2, route))

if __name__ == '__main__':
    main()