from utils import utils

def filter_id(i: int, start: int, end: int):
    return (i >= start) and (i <= end)

def part1(input_data: list[str]) -> int:
    print('-----Part1-----')
    ans: int = 0
    fresh = [id_range.split('-') for id_range in input_data[:input_data.index('')]]
    ingredients = [int(i) for i in input_data[input_data.index('')+1:]]
    fresh_id = []
    for start, end in fresh:
        id_ls = list(filter(lambda i: ((i >= int(start)) and (i <= int(end))), ingredients))
        fresh_id += id_ls
    ans = len(set(fresh_id))
    return ans

def part2(input_data: list[str]) -> int:
    print('-----Part2-----')
    ans: int = 0
    fresh = [id_range.split('-') for id_range in input_data[:input_data.index('')]]
    i = 0
    while i < len(fresh):
        start_1, end_1 = [int(x) for x in fresh[i]]
        j = 0
        o = False
        print(i)
        while j < (len(fresh) - i - 1):
            start_2, end_2 = [int(y) for y in fresh[j + i + 1]]
            overlap = start_1 <= end_2 and start_2 <= end_1
            if overlap:
                fresh[i] = [min(start_1, start_2), max(end_1, end_2)]
                del fresh[j + i + 1]
                o = True
            j += 1
        if not o:
            ans += (int(fresh[i][1]) - int(fresh[i][0]) + 1)
            i += 1
        print(ans)
    return ans
# 345938763603003 l x

def main() -> None:
    print('-----DayN-----')
    input_data: list[str] = utils.read_lines('input.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()