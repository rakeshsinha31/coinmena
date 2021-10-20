import os
from celery import Celery
from datetime import datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coinmena.settings")
app = Celery("coinmena")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "add-every-1-hour": {
        "task": "api.tasks.task_save_quotes",
        "schedule": 10.0,
    }
}

app.conf.timezone = "UTC"
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
