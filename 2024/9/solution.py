from utils import utils

def part1(input_data: str) -> int:
    print('-----Part1-----')
    ans: int = 0
    input_data = list(map(lambda a: int(a), list(input_data)))

    char_index = 0
    flip_flop = True
    disk = []
    for char in input_data:
        if flip_flop:
            # file
            for i in range(char):
                disk.append(int(char_index / 2))
        else:
            # space
            disk.extend(dequeue_blocks(input_data, char))
        flip_flop = not flip_flop
        char_index += 1
    ans = check_sum(disk)
    return ans

def dequeue_blocks(input_data: list[int], no_of_blocks: int, blocks=None) -> list[int]:
    # get list of chars to append
    if blocks is None:
        blocks: list[int] = []
    if no_of_blocks == 0:
        return blocks
    else:
        if input_data[-1] == 0 or len(input_data) % 2 == 0:
            input_data.pop()
        else:
            blocks.append(int(len(input_data) / 2))
            input_data[-1] = input_data[-1] - 1
            no_of_blocks -= 1
        dequeue_blocks(input_data, no_of_blocks, blocks)
    return blocks

def check_sum(disk: list[int]) -> int:
    value: int = 0
    for i in range(len(disk)):
        value += i * disk[i]
    return value

def part2(input_data: str) -> int:
    print('-----Part2-----')
    ans: int = 0
    input_data = list(map(lambda a: int(a), list(input_data)))
    print(input_data)

    char_index = 0
    flip_flop = True
    disk = []
    for char in input_data:
        if flip_flop:
            # file
            for i in range(char):
                disk.append(int(char_index / 2))
        else:
            # space
            disk.extend(dequeue_files(input_data, char))
        flip_flop = not flip_flop
        char_index += 1
    ans = check_sum(disk)
    print(disk)
    # 2858
    # 00992111777.44.333....5555.6666.....8888..
    return ans

def dequeue_file(input_data: list[int], space_len: int, files=None) -> list[int]:
    # get list of chars to append
    # get file len
    # compare
    # repeat
    return files

def dequeue_files(input_data: list[int], no_of_blocks: int, blocks=None) -> list[int]:
    # get list of chars to append, represent space with 0
    if blocks is None:
        blocks: list[int] = []
    if no_of_blocks == 0:
        # pad trailing 0s
        return blocks
    else:
        if input_data[-1] == 0 or len(input_data) % 2 == 0:
            input_data.pop()
        else:
            blocks.append(int(len(input_data) / 2))
            input_data[-1] = input_data[-1] - 1
            no_of_blocks -= 1
        dequeue_files(input_data, no_of_blocks, blocks)
    return blocks

def main() -> None:
    print('-----DayN-----')
    input_data: str = utils.read_str('test.txt')
    # print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()