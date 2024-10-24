import unittest
from solution import *

test_record = Record('test.txt')

class Test_Solution(unittest.TestCase):
    def test_part1(self):
        print('testing part 1...')
        self.assertEqual(part1(test_record), 8)

    def test_part2(self):
        print('testing part 2...')
        self.assertEqual(part2(test_record), 2286)

if __name__ == '__main__':
    unittest.main()