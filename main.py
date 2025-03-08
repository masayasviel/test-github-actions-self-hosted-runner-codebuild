import os

import requests


def main():
    picture_book_number = os.environ['PICTURE_BOOK_NUMBER']
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{picture_book_number}')
    contents = response.json()
    print(contents)


if __name__ == '__main__':
    main()
