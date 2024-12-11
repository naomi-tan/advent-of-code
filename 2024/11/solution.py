from utils import utils

def part1(input_data: list[str]) -> int:
    print('-----Part1-----')
    ans: int = 0
    input_data = list(map(lambda a: int(a), input_data))
    ans = compute_nodes(input_data, 25)
    return ans

def compute_nodes(input_data: list[int], no_blinks: int) -> int:
    # order is preserved but doesn't matter for number of stones count
    # if a number is repeated in the line of stones, all stones will change values in the same way and can be grouped

    # initialise node counts with input data
    node_count = {}
    new_node_count = {}
    # key is number on the stone, value is the number of times the number appears in the line of stones
    for s in input_data:
        increase_dict_value(node_count, s, 1)

    # for every blink
    for b in range(no_blinks):
        new_node_count = {}
        # for every unique number in node count
        for s in node_count:
            # convert 0s to 1s
            if s == 0:
                increase_dict_value(new_node_count, 1, node_count[s])
            # split even number of digits
            elif (len(str(s)) % 2) == 0:
                increase_dict_value(new_node_count, int(str(s)[:int(len(str(s)) / 2)]), node_count[s])
                increase_dict_value(new_node_count, int(str(s)[int(len(str(s)) / 2):]), node_count[s])
            # multiply remaining by 2024
            else:
                increase_dict_value(new_node_count, s * 2024, node_count[s])
        node_count = new_node_count

    # count number of stones by summing counts for all unique numbers
    no_stones = 0
    for n in new_node_count:
        no_stones += new_node_count[n]
    return no_stones

def increase_dict_value(dictionary: dict, key: int, value: int) -> dict:
    # check if key exists in dictionary and increase by value
    if key in dictionary:
        dictionary[key] += value
    else:
        dictionary[key] = value
    return dictionary

def part2(input_data: list[str]) -> int:
    print('-----Part2-----')
    ans: int = 0
    input_data = list(map(lambda a: int(a), input_data))
    ans = compute_nodes(input_data, 75)
    return ans

def main() -> None:
    print('-----DayN-----')
    input_data: list[str] = utils.read_word_arr('input.txt')[0]
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()