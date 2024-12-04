# use dictionary/graph instead of class
from utils.utils import *

class Card:
    def __init__(self, line: str):
        self.id = int(line.split(':')[0].strip().split('Card ')[1])
        self.winning_nums = list(filter(''.__ne__, line.split(':')[1].split('|')[0].split(' ')))
        self.numbers = list(filter(''.__ne__, line.split(':')[1].split('|')[1].split(' ')))
        self.no_of_cards = 1

    def increase(self):
        self.no_of_cards += 1

def part1(input_data: list[str]) -> int:
    print('-----Part1-----')
    total = 0
    for line in input_data:
        winning_nums = list(filter(''.__ne__, line.split(':')[1].split('|')[0].split(' ')))
        your_nums = list(filter(''.__ne__, line.split(':')[1].split('|')[1].split(' ')))
        all_nums = winning_nums + your_nums
        a = len(all_nums)
        b = len(list(set(all_nums)))
        n_matches = a - b
        if n_matches > 0:
            total += pow(2, n_matches - 1)
    return total

def part2(input_data: list[str]) -> int:
    print('-----Part2-----')
    cards = []
    for line in input_data:
        card = Card(line)
        cards.append(card)

    card_no = 0
    total = 0
    for card in cards:
        total += card.no_of_cards
        for n in range(card.no_of_cards):
            n_matches = len(card.winning_nums + card.numbers) - len(list(set(card.winning_nums + card.numbers)))
            for m in range(n_matches):
                cards[card_no + m + 1].increase()
        card_no += 1

    return total

def main() -> None:
    print('-----DayN-----')
    input_data = read_lines('input.txt')
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()