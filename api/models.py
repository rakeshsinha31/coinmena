from django.db import models
from django.contrib.postgres.fields import JSONField


class Quotes(models.Model):
    meta_data = JSONField(default={})
    data = JSONField(default={})
