from utils import utils
import re

def part1(rules: str, pages: list[list[str]]) -> int:
    print('-----Part1-----')
    ans = 0
    for page in pages:
        flag = True
        for p in page:
            # get all rules matching page number
            pattern = '((?:,\d+\||,)' + p + '(?:\|.*?,|,))'
            r_ls = re.findall(pattern, rules)
            for r in r_ls:
                # find position of each number in rule in pages ls
                [r1, r2] = r.replace(',', '').split('|')
                if page.count(r1) > 0:
                    if page.count(r2) > 0:
                        # check rules are followed
                        if page.index(r1) > page.index(r2):
                            flag = False
                            break
            if not flag:
                break
        if flag:
            middle: int = round((len(page) - 1) / 2)
            ans += int(page[middle])
    return ans

def part2(rules: str, pages: list[list[str]]) -> int:
    print('-----Part2-----')
    ans = 0
    return ans

def main() -> None:
    print('-----DayN-----')
    input_data = utils.read_str('test.txt')
    rules: str = ',' + input_data.split('\n\n')[0].replace('\n', ',') + ','
    pages: list[list[str]] = list(map(lambda b: b.split(','), input_data.split('\n\n')[1].split('\n')))
    print(part1(rules, pages))
    print(part2(rules, pages))

if __name__ == '__main__':
    main()