import os
from fetch_input import fetch_input

YEAR = 2024
DAY = 1

if not os.path.isdir(f'../{YEAR}'):
    os.mkdir(f'../{YEAR}')

if not os.path.isdir(f'../{YEAR}/{DAY}'):
    os.mkdir(f'../{YEAR}/{DAY}')

# if not os.path.isfile(f'../{YEAR}/{DAY}/input.txt'):
    # input_data = fetch_input(YEAR, DAY)
    # write to file

# if not os.path.isfile(f'../{YEAR}/{DAY}/solution.py'):
    # write to file

# if not os.path.isfile(f'../{YEAR}/{DAY}/test.txt'):
    # write to file

# if not os.path.isfile(f'../{YEAR}/{DAY}/test.py'):
    # write to file

# if input.txt exists and is not empty do not fetch