"""
Exemple des notions du chapitre 8.
"""


import configparser
import json
import random
from collections import namedtuple
from typing import Dict, List

from twitch_bot import TwitchBot


# Un named tuple est une façon simple de créer des tuples avec des éléments nommés
# (plutôt que juste des index)
ConfigInfo = namedtuple("ConfigInfo", ["nickname", "password", "channel"])


def load_config(filename: str) -> ConfigInfo:
    config = configparser.ConfigParser()
    config.read(filename)
    channel = config.get("chat", "channel")
    bot_nickname = config.get("login", "account_name")
    bot_password = config.get("login", "account_oauth_token")
    return ConfigInfo(bot_nickname, bot_password, channel)


def load_quotes(filename: str) -> Dict[str, List[str]]:
    with open(filename) as f:
        return json.load(f)


def build_quotes_callback(bot: TwitchBot, quotes: Dict[str, List[str]]):
    def callback(*args):
        random_category = random.choice(list(quotes.keys()))
        random_quote = random.choice(quotes[random_category])
        bot.send_privmsg(random_quote)

    return callback


def run_ch8_example(config_filename, quotes_filename):
    config = load_config(config_filename)
    quotes = load_quotes(quotes_filename)
    bot = TwitchBot("logs")
    bot.register_command("quote", build_quotes_callback(bot, quotes))
    bot.connect_and_join(config.password, config.nickname, config.channel)
    bot.run()
