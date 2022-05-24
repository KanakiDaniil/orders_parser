import os
import telebot

import re

bot = telebot.TeleBot("Orders Parser")

parser = re.compile("(\d+)(?:\s*?[^\.\s]*?[\.\s]+)?((?:\S+\s)+?)(\d+(?:ta|та|dona|дона|nafar|нафар)?)?\s?\n?((?:(?:\d+|\s)+)(?:ming|минг|млн|mln|K|k|К/к)?)(?:\.\s?\n?|\s?\n?)((?:.|\n)+?)(\+[\d ]+)\s?\n?([^\n✅❌]+)(✅|❌)")

@bot.message_handler(commands = ["parse"])
def parse (message):
    parsed = parser.findall(message[6:])
    bot.reply_to(message, parsed.__str__())