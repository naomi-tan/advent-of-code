import unittest
from utils.utils import *
import solution

test_data = get_data('test.txt')
expected_result1 = 2
expected_result2 = 4

class TestSolution(unittest.TestCase):

    def test_part1(self):
        print('testing part 1...')
        self.assertEqual(solution.part1(test_data), expected_result1)

    def test_part2(self):
        print('testing part 2...')
        self.assertEqual(solution.part2(test_data), expected_result2)

if __name__ == '__main__':
    unittest.main()