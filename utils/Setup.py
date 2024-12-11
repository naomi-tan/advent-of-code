import os
# get cookie session from browser
# cache data and check before requesting
import urllib3
import requests

session = requests.session()
response2 = session.get('https://adventofcode.com/')
print(response2.text)
print(session.cookies.get_dict())

def fetch_input(year: int, day: int) -> str:
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    cookie = 'session='

    response = urllib3.request(
        'GET',
        url,
        headers={
            'Cookie': cookie
        }
    )

    return response.data.decode('utf-8')
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