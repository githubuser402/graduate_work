import pika
import os
import configparser
import sys

config = configparser.ConfigParser()

if (not bool(config.read(os.path.expanduser('~/.telegram_bot.conf')))):
    sys.exit("Config file not found")


credentials = pika.PlainCredentials(config['rabbitmq']['username'], config['rabbitmq']['password'])
parameters = pika.ConnectionParameters(host=config['rabbitmq']['host'], credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue=config['rabbitmq']['queue'])

message = 'ok'
channel.basic_publish(exchange='', routing_key=config['rabbitmq']['queue'], body=message)

connection.close()
