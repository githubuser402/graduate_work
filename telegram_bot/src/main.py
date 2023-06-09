import asyncio
import pika
from telebot.async_telebot import AsyncTeleBot
from config import config


# Configure your RabbitMQ connection
rabbitmq_credentials = pika.PlainCredentials(config['rabbitmq']['username'], config['rabbitmq']['password'])
rabbitmq_parameters = pika.ConnectionParameters(config['rabbitmq']['host'], credentials=rabbitmq_credentials)

# Configure your Telegram bot
telegram_bot_token = config['telegram']['token']
bot = AsyncTeleBot(telegram_bot_token)


# Define a coroutine for RabbitMQ message consumption
async def consume_rabbitmq():
    connection = pika.BlockingConnection(rabbitmq_parameters)
    channel = connection.channel()
    channel.queue_declare(queue=config['rabbitmq']['queue'])

    def callback(ch, method, properties, body):
        # Process the RabbitMQ message here
        print("Received message:", body.decode())
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='my_queue', on_message_callback=callback)
    channel.start_consuming()


# Define a coroutine for Telegram bot message handling
async def handle_telegram_messages():
    @bot.message_handler(content_types=['text'])
    def handle_message(message):
        # Process the Telegram message here
        print("Received message:", message.text)
        bot.reply_to(message, "I received your message!")

    while True:
        try:
            bot.polling(none_stop=True, interval=1)
        except Exception as e:
            print("Error occurred during Telegram bot polling:", e)
            # Add any necessary error handling or retry logic



# Create an asyncio event loop
event_loop = asyncio.get_event_loop()

# Define tasks for the event loop
telegram_task = event_loop.create_task(bot.polling())
rabbitmq_task = event_loop.run_in_executor(None, consume_rabbitmq)

# Run the event loop
try:
    event_loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    # Clean up resources
    event_loop.run_until_complete(asyncio.gather(telegram_task, return_exceptions=True))
    event_loop.close()