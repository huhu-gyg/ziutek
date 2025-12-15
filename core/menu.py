"""
Навигация по меню
"""
import logging
from telegram import Update
from telegram.ext import ContextTypes

from config import is_authorized, get_user_lang
from locales import get_text
from core.keyboards import (
    BTN_MINE,
    BTN_SHARED,
    BTN_TAROT,
    BTN_TRANSPORT,
    get_persistent_keyboard,
    get_mine_menu_keyboard,
    get_shared_menu_keyboard,
    get_tarot_menu_keyboard,
    get_transport_menu_keyboard,
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
        reply_markup=get_persistent_keyboard()
    )


async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /menu"""
    await start_command(update, context)


async def handle_persistent_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка persistent keyboard кнопок"""
    user_id = update.effective_user.id
    if not is_authorized(user_id):
        await update.message.reply_text("Unauthorized")
        return

    text = update.message.text
    lang = get_user_lang(user_id)

    if text == BTN_MINE:
        await update.message.reply_text(
            f"📝 {get_text(lang, 'menu_mine')}",
            reply_markup=get_mine_menu_keyboard(lang)
        )

    elif text == BTN_SHARED:
        await update.message.reply_text(
            f"📋 {get_text(lang, 'menu_shared')}",
            reply_markup=get_shared_menu_keyboard(lang)
        )

    elif text == BTN_TAROT:
        await update.message.reply_text(
            f"🃏 {get_text(lang, 'menu_tarot')}",
            reply_markup=get_tarot_menu_keyboard(lang)
        )

    elif text == BTN_TRANSPORT:
        await update.message.reply_text(
            f"🚌 {get_text(lang, 'menu_transport')}",
            reply_markup=get_transport_menu_keyboard(lang)
        )


async def handle_menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка inline callback кнопок"""
    query = update.callback_query
    await query.answer()

    user_id = update.effective_user.id
    if not is_authorized(user_id):
        await query.edit_message_text("Unauthorized")
        return

    lang = get_user_lang(user_id)
    data = query.data

    # Подменю Моё
    if data.startswith("mine_"):
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

    # Подменю Транспорт
    elif data.startswith("transport_"):
        await query.edit_message_text(
            f"🚌 TODO",
            reply_markup=get_transport_menu_keyboard(lang)
        )
