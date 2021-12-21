"""
Exemple récapitulatif qui inclut les notions du chapitre 11 et de tous les autres.
"""
from ch8 import load_config
from ch8 import load_quotes
from ch9 import parse_args
from my_bot import MyBot


def run_ch11_example():
    opts = parse_args()

    config = load_config(opts.config_file[0])
    quotes = load_quotes(opts.quotes_file[0])

    bot = MyBot("logs", quotes)
    bot.connect_and_join(config.password, config.nickname, config.channel)
    bot.run()
