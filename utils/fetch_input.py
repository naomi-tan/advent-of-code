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