import re
import math

def read_str(path: str) -> str: # get_raw
    """gets raw data from input.txt file, returns data as a string"""
    file = open(path, 'r')
    data: str = file.read()
    file.close()
    return data

def read_lines(path: str) -> list[str]: # get_data
    """gets data from input.txt file, returns data as a list of strings, each item is a line in the input.txt file"""
    file = open(path, 'r')
    data: list[str] = file.read().split('\n')
    file.close()
    return data

def read_word_arr(path: str) -> list[list[str]]: # get_arr
    """gets data from input.txt file, returns data as a list of strings, each item is a word in the input.txt file"""
    file = open(path, 'r')
    lines: list[str] = file.read().split('\n')
    data: list[list[str]] = []
    for line in lines:
        data.append(line.split())
    file.close()
    return data

def read_csv(path: str) -> list[str]: # get_arr
    """gets data from input.txt file, returns data as a list of strings, each item is a word in the input.txt file"""
    file = open(path, 'r')
    data: list[str] = file.read().split(',')
    file.close()
    return data

def read_char_arr(path: str) -> list[list[str]]: # raw_to_char_arr
    """converts raw input data from list of lines to array of chars, returns list of list of chars"""
    file = open(path, 'r')
    lines: list[str] = file.read().split('\n')
    data: list[list[str]] = []
    for line in lines:
        data.append(list(line))
    file.close()
    return data

def find_nums(line: str) -> list[object]:
    """finds position and value of all numbers (digits) in input string, returns list of re.Match objects"""
    nums = []
    iterator = re.compile(r'\d+')
    for i in iterator.finditer(line):
        nums.append(i)
    return nums

def coerce_in_range(lower: int, upper:int, number: int) -> int:
    """coerce input number to be in specified range"""
    if number < lower:
        return lower
    elif number > upper:
        return upper
    else:
        return number

def in_range(lower: int, upper:int, number: int) -> bool:
    """check if input number is in specified range, returns boolean"""
    if number < lower:
        return False
    elif number > upper:
        return False
    else:
        return True

def get_neighbours(raw_arr: list[list[str]], item_row: int, item_col: int, item_len: int = 1) -> list[str]:
    """returns [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]"""
    num_rows = len(raw_arr)
    num_cols = len(raw_arr[0])
    neighbours: list[str] = []
    # search in y direction
    for i in range(3):
        # search in x direction
        for j in range(item_len + 2):
            row: int = item_row + i - 1
            col: int = item_col - 1 + j
            # if out of range
            if (in_range(0, num_rows - 1, row)) and (in_range(0, num_cols - 1, col)):
                # if self
                if not ((row == item_row) and (in_range(item_col, item_col + item_len - 1, col))):
                    neighbours.append(raw_arr[row][col])
            else:
                neighbours.append('')
    return neighbours

def get_manhattan_neighbours(input_data: list[list[int]], position: list[int]) -> list[int]:
    """returns neighbours top, right, bottom, left"""
    neighbours = []
    n_pos = [[position[0] - 1, position[1]], [position[0], position[1] + 1], [position[0] + 1, position[1]], [position[0], position[1] - 1]]
    for p in n_pos:
        if in_bounds(p, len(input_data), len(input_data[0])):
            neighbours.append(input_data[p[0]][p[1]])
        else:
            neighbours.append(math.nan)
    return neighbours

def in_bounds(pos: list[int], x_max: int, y_max: int) -> bool:
    """check if position is in bounds of array"""
    return (0 <= pos[0] < x_max) and (0 <= pos[1] < y_max)


# parsing, 2d grids, graph algorithms, bfs, dfs, 2d arrays, hash tables (sparse grid (x, y) -> value),
# neighbours (manhattan 4, diagonal 4, all 8), pathfinding, dijkstra, combinations, permutations,
# point rotations
# https://favtutor.com/blogs/breadth-first-search-python
# regex extract numbers from string
# https://www.tutorialspoint.com/extract-decimal-numbers-from-a-string-in-python