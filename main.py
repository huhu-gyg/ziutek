"""
Ziutek Bot - Точка входа
"""
import logging
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters

from config import TELEGRAM_TOKEN
from core.menu import start_command, menu_command, handle_menu_callback, handle_persistent_buttons
from core.keyboards import BTN_MINE, BTN_SHARED, BTN_TAROT, BTN_TRANSPORT

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    """Запуск бота"""
    if not TELEGRAM_TOKEN:
        logger.error("TELEGRAM_TOKEN is not set")
        return

    logger.info("Starting Ziutek Bot...")

    # Создаём приложение
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Команды
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("menu", menu_command))

    # Callback handlers для inline меню
    app.add_handler(CallbackQueryHandler(handle_menu_callback))

    # Handler для persistent keyboard кнопок
    app.add_handler(MessageHandler(
        filters.TEXT & filters.Regex(f"^({BTN_MINE}|{BTN_SHARED}|{BTN_TAROT}|{BTN_TRANSPORT})$"),
        handle_persistent_buttons
    ))

    # TODO: Добавить handlers для модулей
    # - modules.mine.handlers
    # - modules.shared.handlers
    # - modules.tarot.handlers
    # - modules.transport.handlers

    # Запуск
    logger.info("Bot is running...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
