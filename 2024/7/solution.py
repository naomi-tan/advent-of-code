def part1(input_data: list[str]) -> int:
    print('-----Part1-----')
    ans: int = 0
    # representing operators as a number which is then converted to base 4
    # operators = {0: '+', 1: '*', 2: '||'}

    for line in input_data:
        test_val, nums = line.split(':')
        nums = nums.split()

        n_ops: int = (len(nums) - 1) # number of operators is 1 less than number of numbers
        max_ops: int = pow(2, n_ops) # maximum value operators can get

        for ops in range(max_ops):
            operators = list(base10_to_basen(ops, 2).zfill(n_ops), )
            solution = calculate(nums.copy(), operators)
            if solution == int(test_val):
                ans += solution
                break
    return ans

def base10_to_basen(ops: int, base: int) -> str:
    quotient: int = int(ops / base)
    remainder: int = ops % base
    if quotient == 0:
        return str(remainder)
    else:
        return base10_to_basen(quotient, base) + str(remainder)

def calculate(nums: list[str], operators: list[str]) -> int:
    result = nums[0]
    nums.pop(0)
    for i in range(len(operators)):
        result = perform_operation(result, nums[0], operators[0])
        nums.pop(0)
        operators.pop(0)
    return result

def perform_operation(num1: str, num2: str, operator: str) -> int | float:
    # operators = {0: '+', 1: '-', 2: '||'}
    num1 = int(num1)
    num2 = int(num2)
    match operator:
        case '0':
            return num1 + num2
        case '1':
            return num1 * num2
        case '2':
            return int(str(num1) + str(num2))

def part2(input_data: list[str]) -> int:
    print('-----Part2-----')
    ans: int = 0
    for line in input_data:
        test_val, nums = line.split(':')
        nums = nums.split()

        n_ops: int = (len(nums) - 1) # number of operators is 1 less than number of numbers
        max_ops: int = pow(3, n_ops) # maximum value operators can get

        for ops in range(max_ops):
            operators = list(base10_to_basen(ops, 3).zfill(n_ops), )
            solution = calculate(nums.copy(), operators)
            if solution == int(test_val):
                ans += solution
                break
    return ans

def read_lines(path: str) -> list[str]: # get_data
    """gets data from input.txt file, returns data as a list of strings, each item is a line in the input.txt file"""
    file = open(path, 'r')
    data: list[str] = file.read().split('\n')
    file.close()
    return data

def main() -> None:
    print('-----DayN-----')
    input_data: list[str] = read_lines('input.txt')
    print(part1(input_data))
    # print(part2(input_data))

if __name__ == '__main__':
    main()