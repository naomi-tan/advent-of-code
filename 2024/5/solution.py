from utils import utils
import re

def part1(rules: str, updates: list[list[str]]) -> int:
    print('-----Part1-----')
    ans: int = 0
    for update in updates:
        compliant: bool = True
        # list of rules pertaining to update
        rules_ls: list[str] = []
        for page in update:
            # append all rules containing page number to list of rules
            pattern: str = '((?:,\d+\||,)' + page + '(?:\|.*?,|,))'
            rules_ls.extend(re.findall(pattern, rules))
        for r in rules_ls:
            # get numbers listed in rule
            [r1, r2] = r.replace(',', '').split('|')
            # check numbers exist in update
            if update.count(r1) > 0 and update.count(r2) > 0:
                    # find position of each number in rule in pages ls and check rules are followed
                    if update.index(r1) > update.index(r2):
                        compliant = False
                        break
        # check if update follows all rules
        if compliant:
            middle: int = round((len(update) - 1) / 2)
            ans += int(update[middle])
    return ans

def part2(rules: str, updates: list[list[str]]) -> int:
    print('-----Part2-----')
    ans: int = 0
    for update in updates:
        compliant: bool = True
        # list of rules pertaining to update
        rules_ls: list[str] = []
        for page in update:
            # append all rules containing page number to list of rules
            pattern: str = '((?:,\d+\||,)' + page + '(?:\|.*?,|,))'
            rules_ls.extend(re.findall(pattern, rules))
        for r in rules_ls:
            # get numbers listed in rule
            [r1, r2] = r.replace(',', '').split('|')
            # check numbers exist in update
            if update.count(r1) > 0 and update.count(r2) > 0:
                    # find position of each number in rule in pages ls and check rules are followed
                    if update.index(r1) > update.index(r2):
                        compliant = False
                        break
        if not compliant:
            broken: bool = True
            # loop until update is not broken
            while broken:
                fixes: int = 0
                for r in rules_ls:
                    # get numbers listed in rule
                    [r1, r2] = r.replace(',', '').split('|')
                    # check numbers exist in update
                    if update.count(r1) > 0 and update.count(r2) > 0:
                            # find position of each number in rule in pages ls and check rules are followed
                            if update.index(r1) > update.index(r2):
                                # move bad page number to index that follow ruls
                                update.remove(r1)
                                update.insert(update.index(r2), r1)
                                fixes += 1
                # check if update follows all rules
                if fixes == 0:
                    middle: int = round((len(update) - 1) / 2)
                    ans += int(update[middle])
                    broken = False
    return ans

def main() -> None:
    print('-----DayN-----')
    input_data = utils.read_str('input.txt')
    rules: str = ',' + input_data.split('\n\n')[0].replace('\n', ',') + ','
    updates: list[list[str]] = list(map(lambda b: b.split(','), input_data.split('\n\n')[1].split('\n')))
    print(part1(rules, updates))
    print(part2(rules, updates))

if __name__ == '__main__':
    main()