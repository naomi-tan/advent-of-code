# add unittest
# get only find first and last digit

number_dict = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def get_data(path: str) -> str:
    file = open(path, 'r')
    data:str = file.read()
    file.close()
    return data


def get_line_ls(text: str) -> list[str]:
    return text.split('\n')


def part1(lines: list[str]) -> int:
    # split line into list of chars
    total = 0
    for line in lines:
        nums = []
        for char in line:
            # check if char is numeric
            if char.isnumeric():
                nums.append(char)
        # get first and last number, concat and convert to number
        calibration_value = int(nums[0] + nums[-1])
        # add to sum total
        total += calibration_value
    return total


def part2(lines: list[str]) -> int:
    # split line into list of chars
    total = 0
    for line in lines:
        nums = []
        index = 0
        for char in line:
            # check if char is numeric
            if char.isnumeric():
                nums.append(char)
            else:
                line_slice = line[index: index + 5]  # max string length of number word is 5 chars
                for number in number_dict:
                    if line_slice.find(number) == 0:
                        nums.append(str(number_dict[number]))
            index += 1
        # get first and last number, concat and convert to number
        calibration_value = int(nums[0] + nums[-1])
        # add to sum total
        total += calibration_value
    return total


def main() -> None:
    input_data: str = get_data('input.txt')
    lines: list[str] = get_line_ls(input_data)
    print('Part I:')
    print(part1(lines))
    print('Part II:')
    print(part2(lines))


if __name__ == '__main__':
    main()