import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print(os.getenv('TWITCH_CLIENT_ID'))


if __name__ == '__main__':
    main()
