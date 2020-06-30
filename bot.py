import telebot
import os
from flask import Flask, request
from datalayer.album_manager import AlbumManager
from datalayer.user_manager import UserManager
from datalayer.entities.user import User
from datalayer.entities.album import Album

# Telegram bot
token = "1053110908:AAEiWPa7QhzX9l8bvi6-YN4ui82CpHJg1t4"
bot = telebot.TeleBot(token)

user_manager = UserManager()
album_manager = AlbumManager()

# server
server = Flask(__name__)

@server.route('/' + token, methods=['POST'])
def get_message():
	bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
	return "!", 200

@server.route("/")
def webhook():
	bot.remove_webhook()
	bot.set_webhook(url='https://onethousandalbum-bot.herokuapp.com' + TOKEN)
	return "!", 200

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
	print('[/help]')
	message_text = """
	This bot returns you one album from "1001 Albums You Must Hear Before You Die - 2018 Edition" list.
    Send /album to try!
    Send /clear to clear history.
    /help for information
	"""
	bot.send_message(message.chat.id, message_text)

@bot.message_handler(commands=['album'])
def check(message):
	user = User(message)
	if not user_manager.check_user_exists(user):
		user_manager.create_user(user)
		(f"[/album]  User {user.user_id} created")
	user_albums = user_manager.get_user_albums(user)
	album = album_manager.get_random_album(user_albums)
	user_manager.add_album(user, album, user_albums)
	print(f"[/album]  User {user.user_id} got recommendation")
	return bot.send_message(message.chat.id, 'Listen to\n' + str(album), parse_mode='Markdown')

@bot.message_handler(commands=['clear'])
def clear_history(message):
	user = User(message)
	if not user_manager.check_user_exists(user) or len(user_manager.get_user_albums(user)) == 0:
		return bot.send_message(message.chat.id, 'History is empty')
	user_manager.clear_history(user)
	print(f"[/clear]  User {user.user_id} cleared history")
	return bot.send_message(message.chat.id, 'History cleared')
	


if __name__ == "__main__":
   server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))