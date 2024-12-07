from utils import utils

def part1(input_data: list[list[str]]):
    ans = 0
    stop = False
    i = 0
    [direction, position] = get_pos(input_data)
    while not stop and (i < 10000):
        [next_char, stop] = look_ahead(input_data, direction, position)
        if next_char == '#':
            input_data[position[0]][position[1]] = turn(direction)
        elif next_char == '!':
            stop = True
        else: step(input_data, direction, position)
        i += 1
    for line in input_data:
        ans += line.count('x')
    return ans + 1

def get_pos(input_data):
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

def look_ahead(input_data, direction, position):
    stop = False
    if direction == '^':
        next_step = [position[0] - 1, position[1]]
    if direction == '>':
        next_step = [position[0], position[1] + 1]
    if direction == 'v':
        next_step = [position[0] + 1, position[1]]
    if direction == '<':
        next_step = [position[0], position[1] - 1]
    try:
        next_char = input_data[next_step[0]][next_step[1]]
    except:
        next_char = '!'
        stop = True
    return next_char, stop

def step(input_data, direction, position):
    input_data[position[0]][position[1]] = 'x'
    if direction == '^':
        next_step = [position[0] - 1, position[1]]
    if direction == '>':
        next_step = [position[0], position[1] + 1]
    if direction == 'v':
        next_step = [position[0] + 1, position[1]]
    if direction == '<':
        next_step = [position[0], position[1] - 1]
    input_data[next_step[0]][next_step[1]] = direction

def turn(direction):
    dirs = ['^', '>', 'v', '<']
    i = dirs.index(direction) + 1
    try:
        new_dir = dirs[i]
    except:
        new_dir = dirs[0]
    return new_dir

def main() -> None:
    print('-----DayN-----')
    char_arr: list[list[str]] = utils.read_char_arr('input.txt')
    print(part1(char_arr))

if __name__ == '__main__':
    main()