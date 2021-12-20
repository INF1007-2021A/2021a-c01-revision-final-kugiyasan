"""
Fonction principale qui roule les exemples par chapitre.
"""
import argparse
import configparser
import json
import os
import random
import sys
from collections import namedtuple
from dataclasses import dataclass

from ch11 import *
from ch7 import *
from ch8 import *
from ch9 import *
from chatbot import *
from my_bot import MyBot
from twitch_bot import *


def main():
    # chapter_example = "ch8"
    chapter_example = input("Enter 7, 8, 9 or 11: ")
    if chapter_example not in ("7", "8", "9", "11"):
        raise ValueError("Not a valid number")
    chapter_example = "ch" + chapter_example

    if chapter_example == "ch7":
        run_ch7_example()
    elif chapter_example == "ch8":
        run_ch8_example("data/config.ini", "data/quotes.json")
    elif chapter_example == "ch9":
        run_ch9_example()
    elif chapter_example == "ch11":
        run_ch11_example()


if __name__ == "__main__":
    main()
