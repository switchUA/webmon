from telegram import Bot
from argparse import ArgumentParser
import requests

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--token')
    parser.add_argument('--user_id')
    parser.add_argument('--endpoint')
    parser.add_argument('--goal', default=200)
    arguments = parser.parse_args()
    bot = Bot(arguments.token)

    if requests.get(arguments.endpoint).status_code != arguments.goal:
        bot.send_message(arguments.user_id, f"{arguments.endpoint} is not 200")
