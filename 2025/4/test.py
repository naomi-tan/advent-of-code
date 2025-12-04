import unittest
from utils import utils
import solution

test_data = utils.read_char_arr('test.txt')
expected_result1: int = 13
expected_result2: int = 43

class TestSolution(unittest.TestCase):

    def test_part1(self):
        print('testing part 1...')
        self.assertEqual(expected_result1, solution.part1(test_data))

    def test_part2(self):
        print('testing part 2...')
        self.assertEqual(expected_result2, solution.part2(test_data))

if __name__ == '__main__':
    unittest.main()