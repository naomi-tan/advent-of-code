from utils import utils

def part1(input_data: list[str]) -> int:
    print('-----Part1-----')
    ans: int = 0
    input_data = list(map(lambda a: int(a), input_data))
    ans = compute_nodes(input_data, 25)
    return ans

def compute_nodes(input_data: list[int], no_blinks: int) -> int:
    # is it just a graph with cycles?
    node_count = {}
    for s in input_data:
        if s in node_count:
            node_count[s] += 1
        else:
            node_count[s] = 1

    # new_node_count = node_count
    for b in range(no_blinks):
        new_node_count = {}
        for s in node_count:
            if s == 0:
                if 1 in new_node_count:
                    new_node_count[1] += node_count[s]
                else:
                    new_node_count[1] = node_count[s]
                # new_node_count[1] = node_count[s]
            elif (len(str(s)) % 2) == 0:
                if int(str(s)[:int(len(str(s)) / 2)]) in new_node_count:
                    new_node_count[int(str(s)[:int(len(str(s)) / 2)])] += node_count[s]
                else:
                    new_node_count[int(str(s)[:int(len(str(s)) / 2)])] = node_count[s]
                if int(str(s)[int(len(str(s)) / 2):]) in new_node_count:
                    new_node_count[int(str(s)[int(len(str(s)) / 2):])] += node_count[s]
                else:
                    new_node_count[int(str(s)[int(len(str(s)) / 2):])] = node_count[s]
            else:
                if s * 2024 in new_node_count:
                    new_node_count[s * 2024] += node_count[s]
                else:
                    new_node_count[s * 2024] = node_count[s]
        node_count = new_node_count

    no_stones = 0
    for n in new_node_count:
        no_stones += new_node_count[n]
    return no_stones

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