"""
Напоминания через APScheduler
"""
import logging
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

logger = logging.getLogger(__name__)

scheduler = AsyncIOScheduler()


def init_scheduler():
    """Инициализация планировщика"""
    scheduler.start()
    logger.info("Scheduler started")


def add_reminder(run_date: datetime, callback, *args, **kwargs):
    """Добавить напоминание"""
    job = scheduler.add_job(callback, 'date', run_date=run_date, args=args, kwargs=kwargs)
    logger.info(f"Reminder added: {job.id} at {run_date}")
    return job.id


def remove_reminder(job_id: str):
    """Удалить напоминание"""
    scheduler.remove_job(job_id)
    logger.info(f"Reminder removed: {job_id}")


def get_all_reminders():
    """Получить все активные напоминания"""
    return scheduler.get_jobs()
