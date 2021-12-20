"""
Exemple des notions du chapitre 7.
"""
import os
from typing import Callable

from dotenv import load_dotenv

from twitch_bot import TwitchBot

load_dotenv()


def build_say_hi_callback(bot: TwitchBot, message: str) -> Callable[[str], None]:
    def callback(_: str) -> None:
        bot.send_privmsg(message)

    return callback


def run_ch7_example():
    bot = TwitchBot("logs")
    callback = build_say_hi_callback(bot, "hi you betlog")
    bot.register_command("say_hi", callback)

    password = os.environ["password"]
    nickname = os.environ["nickname"]
    channel = os.environ["channel"]
    bot.connect_and_join(password, nickname, channel)
    bot.run()
