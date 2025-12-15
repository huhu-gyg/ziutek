"""
База карт Таро (78 карт Rider-Waite)
"""

# Major Arcana (22 карты)
MAJOR_ARCANA = [
    {
        "id": 0,
        "name": "The Fool",
        "name_ru": "Шут",
        "arcana": "major",
        "keywords": ["начало", "спонтанность", "риск", "невинность"],
        "meaning_upright": "Новое начало, спонтанность, свобода, невинность, приключение",
        "meaning_reversed": "Безрассудство, риск, наивность, глупость",
    },
    {
        "id": 1,
        "name": "The Magician",
        "name_ru": "Маг",
        "arcana": "major",
        "keywords": ["воля", "сила", "действие", "мастерство"],
        "meaning_upright": "Сила воли, творчество, мастерство, концентрация",
        "meaning_reversed": "Манипуляция, обман, неиспользованный потенциал",
    },
    # TODO: Добавить остальные 20 карт Major Arcana
]

# Minor Arcana - Wands (14 карт)
WANDS = [
    # TODO: Ace - King of Wands
]

# Minor Arcana - Cups (14 карт)
CUPS = [
    # TODO: Ace - King of Cups
]

# Minor Arcana - Swords (14 карт)
SWORDS = [
    # TODO: Ace - King of Swords
]

# Minor Arcana - Pentacles (14 карт)
PENTACLES = [
    # TODO: Ace - King of Pentacles
]

# Полная колода
ALL_CARDS = MAJOR_ARCANA + WANDS + CUPS + SWORDS + PENTACLES


def get_card_by_name(name: str) -> dict | None:
    """Найти карту по имени (English или Russian)"""
    name_lower = name.lower()
    for card in ALL_CARDS:
        if card["name"].lower() == name_lower or card["name_ru"].lower() == name_lower:
            return card
    return None


def get_cards_by_arcana(arcana: str) -> list:
    """Получить карты по типу (major, wands, cups, swords, pentacles)"""
    return [card for card in ALL_CARDS if card.get("arcana") == arcana]
