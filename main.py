import requests


def main():
    response = requests.get('https://example.com/')
    contents = response.json()
    print(contents)


if __name__ == '__main__':
    main()
