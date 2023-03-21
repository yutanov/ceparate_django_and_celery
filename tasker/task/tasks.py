from celery import shared_task
from datetime import datetime
from django.core.files.storage import default_storage

from .utils.get_data import extract_data
from .utils.validate import validate_data
from .models import AsyncResults


@shared_task
def check_file(filename, task_id):

    # gettind data from csv
    sn, _print, card_type, pan, momt, mozk = extract_data(filename)

    # validate data
    errors = validate_data(sn, _print, card_type, pan, momt, mozk)

    n_rows = len(sn)

    task = AsyncResults.objects.get(pk=task_id)

    if len(errors) == 0:
        result = "Файл не содержит ошибок"

    else:
        for key, value in errors.items():
            error_str = ""
            s_val = " ".join(value)
            error_str += f"{key} : {s_val} \n"

        result = f"Файл содержит ошибки - {error_str}"

    finished_at = datetime.now()

    task.result = result
    task.n_rows = n_rows
    task.finished_at = finished_at
    task.save()
    default_storage.delete(filename)

    return result
