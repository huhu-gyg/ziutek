"""
Ziutek Bot - Конфигурация
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

# Notion
NOTION_TOKEN = os.getenv("NOTION_TOKEN")

# Авторизованные пользователи
USERS = {
    # user_id: {"name": "...", "lang": "ru|pl|en", "db_prefix": "user1|user2"}
    # Заполнить реальными ID
}

# Notion базы данных
NOTION_DB = {
    # ===== Моё — User 1 =====
    "user1_idea": os.getenv("NOTION_DB_USER1_IDEA", ""),
    "user1_dream": os.getenv("NOTION_DB_USER1_DREAM", ""),
    "user1_zodiac": os.getenv("NOTION_DB_USER1_ZODIAC", ""),
    "user1_todo": os.getenv("NOTION_DB_USER1_TODO", ""),

    # ===== Моё — User 2 =====
    "user2_idea": os.getenv("NOTION_DB_USER2_IDEA", ""),
    "user2_dream": os.getenv("NOTION_DB_USER2_DREAM", ""),
    "user2_zodiac": os.getenv("NOTION_DB_USER2_ZODIAC", ""),
    "user2_todo": os.getenv("NOTION_DB_USER2_TODO", ""),

    # ===== Общее =====
    "shared_travel": os.getenv("NOTION_DB_SHARED_TRAVEL", ""),
    "shared_shopping": os.getenv("NOTION_DB_SHARED_SHOPPING", ""),
    "shared_films": os.getenv("NOTION_DB_SHARED_FILMS", ""),
    "shared_home": os.getenv("NOTION_DB_SHARED_HOME", ""),
    "shared_besha": os.getenv("NOTION_DB_SHARED_BESHA", ""),
    "shared_family": os.getenv("NOTION_DB_SHARED_FAMILY", ""),
    "shared_todo": os.getenv("NOTION_DB_SHARED_TODO", ""),
    "shared_events": os.getenv("NOTION_DB_SHARED_EVENTS", ""),

    # ===== Таро =====
    "tarot_user1": os.getenv("NOTION_DB_TAROT_USER1", ""),
    "tarot_user2": os.getenv("NOTION_DB_TAROT_USER2", ""),
    "tarot_cards": os.getenv("NOTION_DB_TAROT_CARDS", ""),
}


def get_user_db(user_id: int, db_type: str) -> str:
    """Получить ID базы для пользователя"""
    user = USERS.get(user_id)
    if not user:
        return ""
    prefix = user["db_prefix"]
    return NOTION_DB.get(f"{prefix}_{db_type}", "")


def get_shared_db(db_type: str) -> str:
    """Получить ID общей базы"""
    return NOTION_DB.get(f"shared_{db_type}", "")


def is_authorized(user_id: int) -> bool:
    """Проверка авторизации"""
    return user_id in USERS


def get_user_lang(user_id: int) -> str:
    """Получить язык пользователя"""
    user = USERS.get(user_id)
    return user["lang"] if user else "ru"
