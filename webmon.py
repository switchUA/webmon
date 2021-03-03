from telegram import Bot
from argparse import ArgumentParser
import requests

def check_service(endpoint, desired_status):
    try:
        return requests.get(endpoint).status_code == desired_status
    except requests.ConnectionError:
        return False


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('--token')
    parser.add_argument('--user_id')
    parser.add_argument('--endpoint')
    parser.add_argument('--goal', default=200)
    arguments = parser.parse_args()
    bot = Bot(arguments.token)

    if not check_service(arguments.endpoint, arguments.goal):
        bot.send_message(arguments.user_id, f"{arguments.endpoint} is seems to be down")
