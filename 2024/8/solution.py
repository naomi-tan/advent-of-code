from utils import utils
import numpy as np
from itertools import combinations

def part1(input_data: list[list[str]]) -> int:
    print('-----Part1-----')
    ans: int = 0
    input_data = np.array(input_data)

    # get all antenna chars
    [antenna_loc_x, antenna_loc_y] = np.where(input_data != '.')

    # box sort each char locations
    antenna_dict: dict = {}
    for x, y in zip(antenna_loc_x, antenna_loc_y):
        if input_data[x, y].item() in antenna_dict:
            antenna_dict[input_data[x, y].item()].append([x.item(), y.item()])
        else:
            antenna_dict[input_data[x, y].item()] = [[x.item(), y.item()]]

    # get all anti-node locations for all combinations
    anti_node_loc = []
    for key, value in antenna_dict.items():
        combos = combinations(value, 2)
        for c in combos:
            anti_node_loc.extend(get_anti_node_loc(c[0], c[1], input_data.shape))
    ans = len(set(anti_node_loc))
    return ans

def get_anti_node_loc(node1: list[int], node2: list[int], shape:np.array) -> list[tuple]:
    n1 = np.array(node1)
    n2 = np.array(node2)
    d = n2 - n1
    anti_nodes = []
    a1 = n1 - d
    a2 = n1 + 2 * d
    if 0 <= a1[0] < shape[0] and 0 <= a1[1] < shape[1]:
        anti_nodes.append(tuple([a1[0].item(), a1[1].item()]))
    if 0 <= a2[0] < shape[0] and 0 <= a2[1] < shape[1]:
        anti_nodes.append(tuple([a2[0].item(), a2[1].item()]))
    return anti_nodes

def get_harmonic_loc(node1: list[int], node2: list[int], shape:np.array) -> list[tuple]:
    n1 = np.array(node1)
    n2 = np.array(node2)
    d = n2 - n1
    anti_nodes = []
    a1_flag = False
    a2_flag = False
    i = 0
    while not (a1_flag and a2_flag):
        a1 = n1 - i * d
        a2 = n1 + d + i * d
        if 0 <= a1[0] < shape[0] and 0 <= a1[1] < shape[1]:
            anti_nodes.append(tuple([a1[0].item(), a1[1].item()]))
        else:
            a1_flag = True
        if 0 <= a2[0] < shape[0] and 0 <= a2[1] < shape[1]:
            anti_nodes.append(tuple([a2[0].item(), a2[1].item()]))
        else:
            a2_flag = True
        i += 1
    return anti_nodes

def part2(input_data: list[list[str]]) -> int:
    print('-----Part2-----')
    ans: int = 0
    input_data = np.array(input_data)

    # get all antenna chars
    [antenna_loc_x, antenna_loc_y] = np.where(input_data != '.')

    # box sort each char locations
    antenna_dict: dict = {}
    for x, y in zip(antenna_loc_x, antenna_loc_y):
        if input_data[x, y].item() in antenna_dict:
            antenna_dict[input_data[x, y].item()].append([x.item(), y.item()])
        else:
            antenna_dict[input_data[x, y].item()] = [[x.item(), y.item()]]

    # get all anti-node locations for all combinations
    anti_node_loc = []
    for key, value in antenna_dict.items():
        combos = combinations(value, 2)
        for c in combos:
            anti_node_loc.extend(get_harmonic_loc(c[0], c[1], input_data.shape))
    ans = len(set(anti_node_loc))
    return ans

def main() -> None:
    print('-----DayN-----')
    input_data: list[list[str]] = utils.read_char_arr('input.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()