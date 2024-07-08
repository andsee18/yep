from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from test_parser import parse_hh
from .db import save_vacancies, get_analytics

# Функция для обработки команды /start
def start_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to HH Parser Bot! Send me a query to parse HH.ru.')

# Функция для обработки текстовых сообщений
def parse_message(update: Update, context: CallbackContext) -> None:
    user_query = update.message.text
    parsed_vacancies = parse_hh(user_query)
    save_vacancies(parsed_vacancies)
    total_vacancies_in_db = get_analytics()
    update.message.reply_text(f'Parsed {len(parsed_vacancies)} vacancies. Total vacancies in DB: {total_vacancies_in_db}')

# Основная функция для запуска бота
def main():
    bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
    updater = Updater(bot_token)
    dispatcher = updater.dispatcher
    
    # Добавление обработчиков команд и сообщений
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, parse_message))
    
    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()