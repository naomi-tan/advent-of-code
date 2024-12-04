from collections.abc import Mapping

from utils.utils import *

class Range:
    def __init__(self, start: int, length: int):
        self.start = start
        self.end = start + length

class MappedRange:
    def __init__(self, dest_start, source_start, length):
        self.source = Range(source_start, length)
        self.destination = Range(dest_start, length)

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

def seed_pairs(seeds: list[int]) -> list[list[int]]:
    i = 0
    new_seeds = []
    for i in range(int(len(seeds)/2)):
        start = seeds[i*2]
        length = seeds[i*2 + 1]
        new_seeds.append([start, length])
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
    ans = 0
    # start, length
    seeds = list(map(int, input_data[0].split('seeds: ')[1].split(' ')))
    seed_pair_ls = seed_pairs(seeds)
    mapping_arr = input_to_arr(input_data)
    # map gaps to same destination so all locations are mapped

    ##########

    tables = []
    for table in mapping_arr:
        rows = []
        for row in table:
            rows.append(MappedRange(row[0], row[1], row[2]))
            # rows.append([row[1], row[1] + row[2], row[0], row[0] + row[2]])
            # [source start (inc), source end (exc), dest start (inc), dest end(exc)]
        tables.append(rows)
    print(tables[0][0].source.start)

    ##########

    seed_ls = []
    for seed_pair in seed_pair_ls:
        seed_ls.append(Range(seed_pair[0], seed_pair[1]))
    print(seed_ls[0].start)

    ##########

    loc_ls = []

    for seed in seed_ls:
        # for each seed, map seed range to location ranges
        map_out = [seed]
        for table in tables:
            # for each table map input ranges to output ranges
            map_in = map_out
            map_out = []
            for i in map_in:
                for row in table:
                    if row.source.end > i.start >= row.source.start:
                        f =  row.destination.start - row.source.start
                        o_start = i.start + f
                        if row.source.end > i.end >= row.source.start:
                            o_end = i.end + f
                        else:
                            o_end = row.source.end
                            map_in.append(Range(row.source.end, i.end))
                        map_out.append(Range(o_start, o_end))
                        # input [[start, end], ... ]
            loc_ls.append(map_out)
    print(loc_ls)


    # all_seeds = [new_seeds]
    # print(len(tables))
    # print(len(all_seeds))

    # list of seed ranges
    # list of mapped ranges for each table
    # input range in, mapped range out
    # mapped range = input range of next iter
    # loop for all tables

    # for seed in new_seeds:


    i = 0
    # for table in tables:
    #     append_seeds = []
    #     for seed in all_seeds[i]:
    #         if row[1] > seed[0] >= row[0]:
    #
    #     i += 1
    # for seed in all_seeds[i]:
    #     print(seed)
    #     for table in tables:
    #         app_seeds = []
    #         for row in table:
    #             if row[1] > seed[0] >= row[0]:
    #                 app_seeds.append([1, 2, 3, 4])
    #         all_seeds.append(app_seeds)
    # print(all_seeds)


    # map first item, then find first item of any changes in mapping i.e. check where ranges start/end/change
    # for seed in new_seeds:
    #     for table in tables:
    #         for row in table:
    #             if row[1] > seed[0] >= row[0]:
    #                 print(seed, row)
                    # update seed to new location

        # start, end, dstart, dend
        # map first item
        # if in table get end of range of table, map next item
        # if not in table map next item
    return ans

def main() -> None:
    print('-----DayN-----')
    # destination, source, length
    input_data = read_lines('test.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()