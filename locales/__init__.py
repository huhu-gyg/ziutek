"""
Локализация
"""
from locales import ru, pl

LOCALES = {
    "ru": ru.STRINGS,
    "pl": pl.STRINGS,
}


def get_text(lang: str, key: str) -> str:
    """Получить текст на нужном языке"""
    strings = LOCALES.get(lang, LOCALES["ru"])
    return strings.get(key, key)
