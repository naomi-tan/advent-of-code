from utils import utils

def general_solution(input_data: list[list[str]], n: int=1) -> int:
    ans: int = 0
    for line in input_data:
        d_ls = []
        i = -1
        n_len = n
        while n_len > 0:
            search_line = line[(i+1):] if (n_len == 1) else line[(i+1):-(n_len - 1)]
            d = max(search_line)
            d_ls.append(d)
            i += search_line.index(d) + 1
            n_len -= 1
        ans += int(''.join(d_ls))
    return ans

def part1(input_data: list[list[str]]) -> int:
    print('-----Part1-----')
    ans: int = 0
    for line in input_data:
        d1 = max(line[:-1])
        i = line.index(max(line[:-1]))
        d2 = max(line[i+1:])
        ans += int(''.join([d1, d2]))
    # oneline
    # ans = sum([int(''.join([(max(line[:-1])), (max(line[(line.index(max(line[:-1])))+1:]) if (line.index(max(line[:-1]))) > 0 else max(line[1:]))])) for line in input_data])
    # general solution
    # ans = general_solution(input_data, 2)
    return ans

def part2(input_data: list[list[str]]) -> int:
    print('-----Part2-----')
    ans: int = 0
    ans = general_solution(input_data, 12)
    return ans

def main() -> None:
    print('-----DayN-----')
    input_data: list[list[str]] = utils.read_char_arr('input.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()