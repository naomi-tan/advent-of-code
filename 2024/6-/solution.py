from utils import utils
import numpy as np

def part1(char_arr: list[list[str]]) -> int:
    print('-----Part1-----')
    input_data: np.array = np.array(char_arr)
    ans: int = 0
    stop: bool = False
    while not stop:
        # get position and direction of cursor
        [curr_pos, curr_dir] = get_pos(input_data)
        # move until object or edge of map reached
        stop = move(input_data, curr_pos, curr_dir)
        # get new cursor position
        [curr_pos, curr_dir] = get_pos(input_data)
        # turn 90 degrees
        turn(input_data, curr_pos, curr_dir) # maybe bug if cursor is overlayed when edge reached
    ans = count_x(input_data)
    return ans

def get_pos(input_data: np.array) -> list[np.array]:
    # get cursor position and direction
    location: np.array = np.where((input_data == '^') | (input_data == '>') | (input_data == 'v') | (input_data == '<'))
    direction: np.array = input_data[location]
    return [location, direction]

def move(input_data: np.array, curr_pos: np.array, curr_dir: np.array) -> bool:
    # move cursor upto next object or edge
    stop: bool = False
    match curr_dir[0]:
        case '^':
            # get section of line from cursor to edge of map in direction of travel
            line = input_data[:,curr_pos[1]][0:curr_pos[0][0]]
            line = np.flip(line)
            # get new section of line with moved cursor and steps tracked with x
            [new_line, stop] = steps(line, curr_dir)
            new_line = np.flip(new_line)
            # replace section of map with moved cursor and steps tracked with x
            input_data[:curr_pos[0][0]+1, curr_pos[1][0]] = new_line
        case '>':
            line = input_data[curr_pos[0], :][0][curr_pos[1][0] + 1:]
            [new_line, stop] = steps(line, curr_dir)
            input_data[curr_pos[0][0], curr_pos[1][0]:] = new_line
        case 'v':
            line = input_data[:, curr_pos[1]][curr_pos[0][0]+1:]
            [new_line, stop] = steps(line, curr_dir)
            input_data[curr_pos[0][0]:, curr_pos[1][0]] = new_line
        case '<':
            line = input_data[curr_pos[0], :][0][0:curr_pos[1][0]]
            line = np.flip(line)
            [new_line, stop] = steps(line, curr_dir)
            new_line = np.flip(new_line)
            input_data[curr_pos[0][0],:curr_pos[1][0]+1] = new_line
    return stop

def steps(line: np.array, curr_dir: np.array) -> list[np.array, bool]:
    # move upto next object or edge in direction of travel along row or column
    line = np.reshape(line, shape=line.size)
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
    # rotate cursor by 90 degrees
    directions: np.array = np.array(['^', '>', 'v', '<'])
    try:
        new_direction: np.array = directions[np.where(directions == direction[0])[0] + 1]
    except IndexError:
        new_direction: np.array = directions[0]
    input_data[curr_pos] = new_direction[0]
    return new_direction

def count_x(input_data: np.array) -> int:
    # count number of steps taken
    return np.where(input_data == 'x')[0].size

def part2(char_arr: list[list[str]]) -> int:
    print('-----Part2-----')
    # place obstruction on x marked spot from part1
    # if hit edge stop
    # if repeating path stop??
    raw_data: np.array = np.array(char_arr)
    input_data: np.array = np.array(char_arr)
    ans: int = 0
    stop: bool = False
    while not stop:
        # get position and direction of cursor
        [curr_pos, curr_dir] = get_pos(input_data)
        # move until object or edge of map reached
        stop = move(input_data, curr_pos, curr_dir)
        # get new cursor position
        [curr_pos, curr_dir] = get_pos(input_data)
        # turn 90 degrees
        turn(input_data, curr_pos, curr_dir)  # maybe bug if cursor is overlayed when edge reached
    x_pos = np.where(input_data == 'x')
    new_input = np.copy(input_data)
    new_input[x_pos[0][0], x_pos[1][0]] = '#'
    print(new_input)
    return ans

def check_loop(input_data: np.array):
    ans: int = 0
    stop: bool = False
    while not stop:
        # get position and direction of cursor
        [curr_pos, curr_dir] = get_pos(input_data)
        # move until object or edge of map reached
        stop = move(input_data, curr_pos, curr_dir)
        # get new cursor position
        [curr_pos, curr_dir] = get_pos(input_data)
        # turn 90 degrees
        turn(input_data, curr_pos, curr_dir)  # maybe bug if cursor is overlayed when edge reached
    x_pos = np.where(input_data == 'x')

def main() -> None:
    print('-----DayN-----')
    char_arr: list[list[str]] = utils.read_char_arr('input.txt')
    print(part1(char_arr))
    # print(part2(char_arr))

if __name__ == '__main__':
    main()