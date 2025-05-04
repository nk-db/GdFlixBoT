from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

def start(update, context):
    update.message.reply_text("Send me a movie or show name!")

def search_gdflix(update, context):
    query = update.message.text.strip()
    link = f"https://gdflix.pro/search/{query.replace(' ', '%20')}"
    update.message.reply_text(f"Here's your GDFlix link:\n{link}")

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, search_gdflix))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
