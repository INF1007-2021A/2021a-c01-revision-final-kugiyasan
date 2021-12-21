"""
Exemple des notions du chapitre 9.
"""
import argparse
import sys

from ch8 import run_ch8_example


def parse_args():
    arg_parser = argparse.ArgumentParser(
        description="Run custom chatbot.", epilog="Made by me."
    )
    arg_parser.add_argument(
        "--config-file",
        dest="config_file",
        action="store",
        nargs=1,
        type=str,
        metavar="INI_FILE",
        help="The INI file containing login and target chat information.",
    )
    arg_parser.add_argument(
        "--quotes-file",
        dest="quotes_file",
        action="store",
        nargs=1,
        type=str,
        metavar="JSON_FILE",
        help="The JSON file containing the various quotes "
        "supported by the !quote command.",
    )
    return arg_parser.parse_args(sys.argv[1:])


def run_ch9_example():
    opts = parse_args()
    run_ch8_example(opts.config_file[0], opts.quotes_file[0])
