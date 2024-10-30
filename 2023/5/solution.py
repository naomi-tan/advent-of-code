from utils.utils import *

def input_to_arr(input_data: list[str]) -> list[list[list[int]]]:
    flag = 0
    arr = []
    while flag == 0:
        try:
            start = input_data.index('')
        except:
            start = 0
        temp = input_data[start + 2: len(input_data)]
        try:
            end = temp.index('')
        except:
            end = len(input_data) - start + 2
            flag = 1
        mapping = list(map(lambda a: list(map(int, a.split(' '))), input_data[start + 2 : start + 2 + end]))
        arr.append(mapping)
        input_data = temp
    return arr

def seed_to_location(mapping_arr: list[list[list[int]]], seed: int) -> int:
    location = seed
    for mapping in mapping_arr:
        output = seed
        for line in mapping:
            destination = line[0]
            source = line[1]
            length = line[2]
            if source <= seed < source + length:
                i = seed - source
                output = destination + i
                break
        seed = output
        location = output
    return location

def seed_range(seeds: list[int]) -> list[int]:
    i = 0
    new_seeds = []
    for i in range(int(len(seeds)/2)):
        start = seeds[i*2]
        length = seeds[i*2 + 1]
        for j in range(length):
            new_seeds.append(start + j)
    return new_seeds

def part1(input_data: list[str]) -> int:
    print('-----Part1-----')
    seeds = list(map(int, input_data[0].split('seeds: ')[1].split(' ')))
    mapping_arr = input_to_arr(input_data)
    locations = []
    i = 0
    for seed in seeds:
        locations.append(seed_to_location(mapping_arr, seeds[i]))
        i += 1
    ans = min(locations)
    return ans

def part2(input_data: list[str]) -> int:
    print('-----Part2-----')
    seeds = list(map(int, input_data[0].split('seeds: ')[1].split(' ')))
    new_seeds = seed_range(seeds)
    print(new_seeds)
    mapping_arr = input_to_arr(input_data)
    locations = []
    i = 0
    for seed in new_seeds:
        locations.append(seed_to_location(mapping_arr, new_seeds[i]))
        i += 1
    ans = min(locations)
    return ans

def main() -> None:
    print('-----DayN-----')
    input_data = get_data('input.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()