"""
Handlers для модуля 'Таро'
"""
import logging
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

# TODO: Реализовать handlers для:
# - daily (карта дня) - загрузка фото, распознавание, сохранение
# - diary (дневник) - поиск по дате, карте, слову
# - stats (статистика) - месяц, год, всё время
# - cards_db (база карт) - просмотр 78 карт
