from __future__ import absolute_import, unicode_literals
from baseplate.celery import app


@app.task
def add():
    print("aaaa")
