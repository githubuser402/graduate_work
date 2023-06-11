from django.core.management.base import BaseCommand
import telebot
from django.conf import settings
import os
from menu.models import Restaurant
from menu.services import get_user_from_token
from menu.models import Restaurant, Category, Menu, Dish

bot = telebot.TeleBot(token=settings.TELEGRAM_BOT_TOKEN)


def send_message(user, sender, db_object, status):
    if not user.telegram_id:
        return
    
    if sender == 'Restaurant':
        if status == 'created':
            bot.send_message(user.telegram_id, f"Ресторан {db_object.name} створено")
        elif status == 'deleted':
            bot.send_message(user.telegram_id, f"Ресторан {db_object.name} видалено")

    elif sender == 'Menu':
        restaurant_name = db_object.restaurant.name
        if status == 'created':
            bot.send_message(user.telegram_id, f"Меню {db_object.title} створено в ресторані {restaurant_name}")
        elif status == 'deleted':
            bot.send_message(user.telegram_id, f"Меню {db_object.title} видалено в ресторані {restaurant_name}")

    elif sender == 'Category':
        menu_title = db_object.menu.title
        restaurant_name = db_object.menu.restaurant.name

        if status == 'created':
            bot.send_message(user.telegram_id, f"Категорію {db_object.title} створено в меню {menu_title} ресторану {restaurant_name}")
        elif status == 'deleted':
            bot.send_message(user.telegram_id, f"Категорію {db_object.title} видалено в меню {menu_title} ресторану {restaurant_name}")

    elif sender == 'Dish':
        menu_title = db_object.menu.title
        restaurant_name = db_object.menu.restaurant.name

        if status == 'created':
            bot.send_message(user.telegram_id, f"Страву {db_object.name} створено в меню {menu_title} ресторану {restaurant_name}")
        elif status == 'deleted':
            bot.send_message(user.telegram_id, f"Страву {db_object.name} видалено в меню {menu_title} ресторану {restaurant_name}")


class Command(BaseCommand):
    help = "Run telegram bot"

    def handle(self, *args, **options):

        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            bot.send_message(message.chat.id, f"Ласкаво просимо до бота для керування меню ресторану.\nДля початку роботи увійдіть в акаунт. \nВикористайте /help для допомоги")

        @bot.message_handler(commands=['help'])
        def help_message(message):
            bot.send_message(message.chat.id, "/modifymenu - надсилає посилання на сайт для редагування меню\n/login <токен> - використовується для входу в акаунт\nТокен можливо отримати на веб сторінці адміністратора\n/help - допомога ")


        @bot.message_handler(content_types=['text'])
        def login(message):
            if message.text.startswith('/login'):
                try: 
                    token = message.text.split(' ')[1]
                except IndexError:
                    bot.send_message(message.chat.id, "Будь ласка, введіть токен")
                    return
                
                try:
                    user = get_user_from_token(token)
                    if message.chat.type == 'group' or message.chat.type == 'supergroup':
                        user.telegram_id = message.chat.id
                        user.save()
                        bot.send_message(message.chat.id, f"Ви увійшли в акаунт як {user.first_name} {user.last_name}")
                    else:
                        bot.send_message(message.chat.id, "Будь ласка, додайте бота до групи")
                except Exception as e:
                    bot.send_message(message.chat.id, f"something went wrong, try again")


        @bot.message_handler(commands=['modifymenu'])
        def modify_menu(message):
            with open(os.path.join(settings.STATIC_ROOT, 'menu_management_system_logo.jpeg'), 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption="localhost:5173/admin/")

        bot.polling()
