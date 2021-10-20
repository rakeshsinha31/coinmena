# from celery.task.schedules import crontab
from celery import shared_task
from api.views import save_quotes


@shared_task
def task_save_quotes():
    """
    Saves quotes
    """
    save_quotes()
    print("Saved quotes")
