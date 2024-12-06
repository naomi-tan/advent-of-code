from utils import utils
import numpy as np

def part1(char_arr: list[list[str]]) -> int:
    print('-----Part1-----')
    input_data: np.array = np.array(char_arr)
    ans: int = 0
    stop: bool = False
    while not stop:
        [curr_pos, curr_dir] = get_pos(input_data)
        stop = move(input_data, curr_pos, curr_dir)
        [curr_pos, curr_dir] = get_pos(input_data)
        turn(input_data, curr_pos, curr_dir)
    ans = count_x(input_data)
    return ans

def get_pos(input_data: np.array) -> list[np.array]:
    location: np.array = np.where((input_data == '^') | (input_data == '>') | (input_data == 'v') | (input_data == '<'))
    direction: np.array = input_data[location]
    return [location, direction]

def move(input_data: np.array, curr_pos: np.array, curr_dir: np.array) -> bool:
    stop: bool = False
    match curr_dir[0]:
        case '^':
            line = input_data[:,curr_pos[1]][0:curr_pos[0][0]]
            line = np.flip(line)
            line = np.reshape(line, shape=line.size)
            [new_line, stop] = steps(line, curr_dir)
            new_line = np.flip(new_line)
            input_data[:curr_pos[0][0]+1, curr_pos[1][0]] = new_line
        case '>':
            line = input_data[curr_pos[0], :][0][curr_pos[1][0] + 1:]
            line = np.reshape(line, shape=line.size)
            [new_line, stop] = steps(line, curr_dir)
            input_data[curr_pos[0][0], curr_pos[1][0]:] = new_line
        case 'v':
            line = input_data[:, curr_pos[1]][curr_pos[0][0]+1:]
            line = np.reshape(line, shape=line.size)
            [new_line, stop] = steps(line, curr_dir)
            input_data[curr_pos[0][0]:, curr_pos[1][0]] = new_line
        case '<':
            line = input_data[curr_pos[0], :][0][0:curr_pos[1][0]]
            line = np.flip(line)
            line = np.reshape(line, shape=line.size)
            [new_line, stop] = steps(line, curr_dir)
            new_line = np.flip(new_line)
            input_data[curr_pos[0][0],:curr_pos[1][0]+1] = new_line
    # print(input_data)
    return stop

def steps(line: np.array, curr_dir: np.array) -> list[np.array, bool]:
    stop: bool = False
    obstacle: np.array = np.where(line == '#')
    if len(obstacle[0]) == 0:
        line: np.array = np.full(line.size, 'x')
        stop = True
    else:
        line[:obstacle[0][0]] = np.full((obstacle[0][0]), 'x')
        line[obstacle[0][0] - 1] = curr_dir[0]
    # append x to start for cursor start position
    line: np.array = np.insert(line, 0,'x')
    return [line, stop]

def turn(input_data: np.array, curr_pos: np.array, direction: np.array) -> np.array:
    directions: np.array = np.array(['^', '>', 'v', '<'])
    try:
        new_direction: np.array = directions[np.where(directions == direction[0])[0] + 1]
    except IndexError:
        new_direction: np.array = directions[0]
    input_data[curr_pos] = new_direction[0]
    return new_direction

def count_x(input_data: np.array) -> int:
    return np.where(input_data == 'x')[0].size

def part2(input_data: list[list[str]]) -> int:
    print('-----Part2-----')
    ans: int = 0
    return ans

def main() -> None:
    print('-----DayN-----')
    char_arr: list[list[str]] = utils.read_char_arr('input.txt')
    print(part1(char_arr))
    # print(part2(input_data))

if __name__ == '__main__':
    main()