import configparser
import sys
import os

config = configparser.ConfigParser()

if (not bool(config.read(os.path.expanduser('~/.telegram_bot.conf')))):
    sys.exit("Config file not found")
