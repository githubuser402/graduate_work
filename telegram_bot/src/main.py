#!/usr/bin/env python
import telebot
from telebot import types
import configparser
import os
import sys
import pika 

config = configparser.ConfigParser()

if(not bool(config.read(os.path.expanduser('~/.telegram_bot.conf')))):
    sys.exit("Config file not found")

credentials = pika.PlainCredentials(config['rabbitmq']['username'], config['rabbitmq']['password'])
parameters = pika.ConnectionParameters(host=config['rabbitmq']['host'], credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='changes_queue')

bot = telebot.TeleBot(token=config['telegram']['token'])

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to our Menu Management Bot!\We're here to simplify menu management for your restaurant. With our bot, you can easily create, update, and customize your menu offerings. Visit [website_link] to access our menu management system.\
    Use '/help' for a list of commands and their functionalities. We're here to guide you through the process and provide prompt support.\
    Thank you for choosing our Menu Management Bot. Let's create a captivating menu together!")

def changes_processor(ch, method, properties, body):
    print(body)

channel.basic_consume(queue='changes_queue', on_message_callback=changes_processor, auto_ack=True)

@bot.message_handler(commands=['menu'])
def menu(message):
    bot.send_message(message.chat.id, "") 

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=1)
