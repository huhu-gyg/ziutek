"""
Фабрики клавиатур
"""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from locales import get_text


def get_main_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    """Главное меню"""
    keyboard = [
        [InlineKeyboardButton(f"📝 {get_text(lang, 'menu_mine')}", callback_data="menu_mine")],
        [InlineKeyboardButton(f"📋 {get_text(lang, 'menu_shared')}", callback_data="menu_shared")],
        [InlineKeyboardButton(f"🃏 {get_text(lang, 'menu_tarot')}", callback_data="menu_tarot")],
        [InlineKeyboardButton(f"🚌 {get_text(lang, 'menu_bus')}", callback_data="menu_bus")],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_mine_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    """Меню 'Моё'"""
    keyboard = [
        [InlineKeyboardButton(f"💡 {get_text(lang, 'mine_idea')}", callback_data="mine_idea")],
        [InlineKeyboardButton(f"🌙 {get_text(lang, 'mine_dream')}", callback_data="mine_dream")],
        [InlineKeyboardButton(f"♈ {get_text(lang, 'mine_zodiac')}", callback_data="mine_zodiac")],
        [InlineKeyboardButton(f"✅ {get_text(lang, 'mine_todo')}", callback_data="mine_todo")],
        [InlineKeyboardButton(f"⬅️ {get_text(lang, 'back')}", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_shared_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    """Меню 'Общее'"""
    keyboard = [
        [
            InlineKeyboardButton(f"✈️ {get_text(lang, 'shared_travel')}", callback_data="shared_travel"),
            InlineKeyboardButton(f"🛒 {get_text(lang, 'shared_shopping')}", callback_data="shared_shopping"),
        ],
        [
            InlineKeyboardButton(f"🎬 {get_text(lang, 'shared_films')}", callback_data="shared_films"),
            InlineKeyboardButton(f"🏠 {get_text(lang, 'shared_home')}", callback_data="shared_home"),
        ],
        [
            InlineKeyboardButton(f"🐕 {get_text(lang, 'shared_besha')}", callback_data="shared_besha"),
            InlineKeyboardButton(f"👨‍👩‍👧 {get_text(lang, 'shared_family')}", callback_data="shared_family"),
        ],
        [
            InlineKeyboardButton(f"✅ {get_text(lang, 'shared_todo')}", callback_data="shared_todo"),
            InlineKeyboardButton(f"📅 {get_text(lang, 'shared_events')}", callback_data="shared_events"),
        ],
        [InlineKeyboardButton(f"⬅️ {get_text(lang, 'back')}", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_tarot_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    """Меню 'Таро'"""
    keyboard = [
        [InlineKeyboardButton(f"🎴 {get_text(lang, 'tarot_daily')}", callback_data="tarot_daily")],
        [InlineKeyboardButton(f"📖 {get_text(lang, 'tarot_diary')}", callback_data="tarot_diary")],
        [InlineKeyboardButton(f"📊 {get_text(lang, 'tarot_stats')}", callback_data="tarot_stats")],
        [InlineKeyboardButton(f"🎴 {get_text(lang, 'tarot_cards_db')}", callback_data="tarot_cards_db")],
        [InlineKeyboardButton(f"⬅️ {get_text(lang, 'back')}", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_bus_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    """Меню 'Автобусы'"""
    keyboard = [
        [InlineKeyboardButton("🔍 Найти маршрут", callback_data="bus_search")],
        [InlineKeyboardButton("⭐ Избранные", callback_data="bus_favorites")],
        [InlineKeyboardButton("🕐 Ближайшие", callback_data="bus_nearest")],
        [InlineKeyboardButton(f"⬅️ {get_text(lang, 'back')}", callback_data="menu_main")],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_back_keyboard(lang: str, callback_data: str = "menu_main") -> InlineKeyboardMarkup:
    """Кнопка 'Назад'"""
    keyboard = [
        [InlineKeyboardButton(f"⬅️ {get_text(lang, 'back')}", callback_data=callback_data)],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_save_cancel_keyboard(lang: str) -> InlineKeyboardMarkup:
    """Кнопки сохранить/отмена"""
    keyboard = [
        [
            InlineKeyboardButton(f"💾 {get_text(lang, 'save')}", callback_data="action_save"),
            InlineKeyboardButton(f"❌ {get_text(lang, 'cancel')}", callback_data="action_cancel"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
