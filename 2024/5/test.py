import unittest
from utils import utils
import solution

input_data = utils.read_str('test.txt')
rules: str = ',' + input_data.split('\n\n')[0].replace('\n', ',') + ','
pages: list[list[str]] = list(map(lambda b: b.split(','), input_data.split('\n\n')[1].split('\n')))
expected_result1 = 143
expected_result2 = 123

class TestSolution(unittest.TestCase):

    def test_part1(self):
        print('testing part 1...')
        self.assertEqual(solution.part1(rules, pages), expected_result1)

    def test_part2(self):
        print('testing part 2...')
        self.assertEqual(solution.part2(rules, pages), expected_result2)

if __name__ == '__main__':
    unittest.main()