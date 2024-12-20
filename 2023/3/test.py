import unittest
from utils.utils import *
from solution import *

test_data = read_lines('test.txt')
test_arr = read_char_arr('test.txt')
expected_result1 = 4361
expected_result2 = 467835

class TestSolution(unittest.TestCase):

    def test_part1(self):
        print('testing part 1...')
        self.assertEqual(part1(test_data, test_arr), expected_result1)

    def test_part2(self):
        print('testing part 2...')
        self.assertEqual(part2(test_data, test_arr), expected_result2)

if __name__ == '__main__':
    unittest.main()