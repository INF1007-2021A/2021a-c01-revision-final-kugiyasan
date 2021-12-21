"""
Un chatbot qui s'identifie et donnes des citations aléatoires.
"""
import random
from typing import Dict
from typing import List

from chatbot import Chatbot
from twitch_bot import TwitchBot


class MyBot(TwitchBot):
    __slots__ = ("quotes",)

    def __init__(self, logs_folder: str, quotes: Dict[str, List[str]]) -> None:
        super().__init__(logs_folder)
        self.quotes = quotes

    @TwitchBot.new_command
    def say_hi(self, cmd: Chatbot.Command) -> None:
        txt = f"My name is {self.nickname}. You killed my father. Prepare to die."
        self.send_privmsg(txt)

    @TwitchBot.new_command
    def quote(self, cmd: Chatbot.Command) -> None:
        random_category = cmd.params or random.choice(list(self.quotes.keys()))
        if random_category not in self.quotes:
            self.send_privmsg("This character doesn't exist dumdum")
            return

        random_quote = random.choice(self.quotes[random_category])
        self.send_privmsg(random_quote)
