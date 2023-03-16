from celery import Celery
import requests
import json
import os

REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_PORT = os.environ["REDIS_PORT"]
API = os.environ['API']

redis_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
app = Celery("tasks", broker=redis_url, backend=redis_url)


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
    "sum_numbers_API": {"task": "tasks.sum_numbers_API", "schedule": 15.0}
}
app.conf.timezone = "UTC"
