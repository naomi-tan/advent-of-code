import re

def get_data(path: str) -> list[str]:
    """gets data from input.txt file, returns data as a list of strings, each item is a line in the input.txt file"""
    file = open(path, 'r')
    data: list[str] = file.read().split('\n')
    file.close()
    return data

def raw_to_char_arr(raw: list[str]) -> list[list[str]]:
    """converts raw input data from list of lines to array of chars, returns list of list of chars"""
    char_arr = []
    for line in raw:
        char_arr.append(list(line))
    return char_arr

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

def get_neighbours(raw_arr: list[list[str]], item_row: int, item_col: int, item_len: int) -> list[str]:
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


# parsing, 2d grids, graph algorithms, bfs, dfs, 2d arrays, hash tables (sparse grid (x, y) -> value),
# neighbours (manhattan 4, diagonal 4, all 8), pathfinding, dijkstra, combinations, permutations,
# point rotations
# https://favtutor.com/blogs/breadth-first-search-python
# regex extract numbers from string
# https://www.tutorialspoint.com/extract-decimal-numbers-from-a-string-in-python