# implement unittest
# oop

import test


class Record:
    def __init__(self, path: str):
        self.path = path
        self.raw = self.get_data()
        self.num_games = self.get_num_games()

    def get_data(self) -> str:
        file = open(self.path, 'r')
        data: str = file.read()
        file.close()
        return data

    def get_num_games(self) -> int:
        return len(self.raw.split('\n'))

    def game(self, n: int):
        game_data = self.raw.split('\n')[n - 1].split(':')[1]
        return Game(game_data)


class Game:
    def __init__(self, raw: str):
        self.raw = raw
        self.num_turns = self.get_num_turns()

    def get_num_turns(self) -> int:
        return len(self.raw.split(';'))

    def turn(self, n: int):
        turn_data = self.raw.split(';')[n - 1]
        return Turn(turn_data)


class Turn:
    def __init__(self, raw: str):
        self.raw = raw
        self.red = self.count('red')
        self.green = self.count('green')
        self.blue = self.count('blue')

    def __str__(self):
        return self.raw

    def count(self, colour: str) -> int:
        n = 0
        ls = self.raw.split(',')
        for l in ls:
            if l.find(colour) >= 0:
                l = l.lower()
                n_str = l.replace(colour, '')
                n = int(n_str)
        return n


def check_valid_turn(max_turn: Turn, turn: Turn) -> bool:
    valid = True
    if turn.red > max_turn.red:
        valid = False
    if turn.green > max_turn.green:
        valid = False
    if turn.blue > max_turn.blue:
        valid = False
    return valid


def get_max_turn(game: Game) -> Turn:
    red = 0
    green = 0
    blue = 0
    for i in range(game.num_turns):
        if game.turn(i + 1).red > red:
            red = game.turn(i + 1).red
        if game.turn(i + 1).green > green:
            green = game.turn(i + 1).green
        if game.turn(i + 1).blue > blue:
            blue = game.turn(i + 1).blue
    return Turn(f'{red} red, {green} green, {blue} blue')


def part1(test_record: Record) -> int:
    max_turn = Turn('12 red, 13 green, 14 blue')
    valid_ids = []
    for i in range(test_record.num_games):
        valid = True
        for j in range(test_record.game(i + 1).num_turns):
            if check_valid_turn(max_turn, test_record.game(i + 1).turn(j + 1)) == False:
                valid = False
        if valid:
            valid_ids.append(i + 1)
    print(sum(valid_ids))
    return sum(valid_ids)


def part2(test_record: Record) -> int:
    powers = []
    for i in range(test_record.num_games):
        max_turn = get_max_turn(test_record.game(i + 1))
        power = max_turn.red * max_turn.green * max_turn.blue
        powers.append(power)
    print(sum(powers))
    return sum(powers)


def main() -> None:
    test_record = Record('input.txt')
    part1(test_record)
    part2(test_record)


if __name__ == '__main__':
    main()