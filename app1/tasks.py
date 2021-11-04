from __future__ import absolute_import, unicode_literals

from celery import shared_task
from time import sleep

@shared_task
def add(x, y):
    sleep(3)
    return x + y