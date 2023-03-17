from celery import Celery
import requests
import json
import os

API = os.environ["API"]

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tasker.settings")

app = Celery("tasker")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task
def sum_numbers_API():
    response = requests.get(API)
    data_get = response.json()

    for el in data_get:
        el_data = {}
        number_sum = el.get("number_sum")
        if number_sum:
            pass
        else:
            number_one = el.get("number_one")
            number_two = el.get("number_two")
            el["number_sum"] = number_one + number_two
            el_data = json.dumps(el)
            r_put = requests.put(API, data=el_data)
            if r_put.status_code == 202:
                pass
            else:
                print(f"Error: status code {r_put.status_code}")


app.conf.beat_schedule = {
    "sum_numbers_API": {"task": "task.celery.sum_numbers_API", "schedule": 15.0}
}
app.conf.timezone = "UTC"
