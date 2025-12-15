"""
Навигация по меню
"""
import logging
from telegram import Update
from telegram.ext import ContextTypes

from config import is_authorized, get_user_lang
from locales import get_text
from core.keyboards import (
    get_main_menu_keyboard,
    get_mine_menu_keyboard,
    get_shared_menu_keyboard,
    get_tarot_menu_keyboard,
    get_bus_menu_keyboard,
)

logger = logging.getLogger(__name__)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /start"""
    user_id = update.effective_user.id

    if not is_authorized(user_id):
        await update.message.reply_text("Unauthorized")
        return

    lang = get_user_lang(user_id)
    await update.message.reply_text(
        get_text(lang, "main_menu"),
        reply_markup=get_main_menu_keyboard(lang)
    )


async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /menu"""
    await start_command(update, context)


async def handle_menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка навигации по меню"""
    query = update.callback_query
    await query.answer()

    user_id = update.effective_user.id
    if not is_authorized(user_id):
        await query.edit_message_text("Unauthorized")
        return

    lang = get_user_lang(user_id)
    data = query.data

    if data == "menu_main":
        await query.edit_message_text(
            get_text(lang, "main_menu"),
            reply_markup=get_main_menu_keyboard(lang)
        )

    elif data == "menu_mine":
        await query.edit_message_text(
            f"📝 {get_text(lang, 'menu_mine')}",
            reply_markup=get_mine_menu_keyboard(lang)
        )

    elif data == "menu_shared":
        await query.edit_message_text(
            f"📋 {get_text(lang, 'menu_shared')}",
            reply_markup=get_shared_menu_keyboard(lang)
        )

    elif data == "menu_tarot":
        await query.edit_message_text(
            f"🃏 {get_text(lang, 'menu_tarot')}",
            reply_markup=get_tarot_menu_keyboard(lang)
        )

    elif data == "menu_bus":
        await query.edit_message_text(
            f"🚌 {get_text(lang, 'menu_bus')}",
            reply_markup=get_bus_menu_keyboard(lang)
        )

    # Подменю Моё
    elif data.startswith("mine_"):
        module = data.replace("mine_", "")
        await query.edit_message_text(
            f"📝 {get_text(lang, f'mine_{module}')} - TODO",
            reply_markup=get_mine_menu_keyboard(lang)
        )

    # Подменю Общее
    elif data.startswith("shared_"):
        module = data.replace("shared_", "")
        await query.edit_message_text(
            f"📋 {get_text(lang, f'shared_{module}')} - TODO",
            reply_markup=get_shared_menu_keyboard(lang)
        )

    # Подменю Таро
    elif data.startswith("tarot_"):
        action = data.replace("tarot_", "")
        await query.edit_message_text(
            f"🃏 {get_text(lang, f'tarot_{action}')} - TODO",
            reply_markup=get_tarot_menu_keyboard(lang)
        )

    # Подменю Автобусы
    elif data.startswith("bus_"):
        await query.edit_message_text(
            "🚌 TODO",
            reply_markup=get_bus_menu_keyboard(lang)
        )
