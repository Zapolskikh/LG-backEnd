import sqlite3

connection = sqlite3.connect('words_game.db')

cursor = connection.cursor()

command_create_usrs = """CREATE TABLE users(user_id INTEGER PRIMARY KEY, user_name TEXT)"""
command_create_words = """CREATE TABLE words(word_id INTEGER PRIMARY KEY, word_name_cource TEXT, word_name_trans TEXT, current_user_id INTEGER, FOREIGN KEY(current_user_id) REFERENCES users(user_id))"""
cursor.execute(command_create_usrs)
cursor.execute(command_create_words)
