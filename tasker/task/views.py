from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.files.storage import default_storage
from datetime import datetime

from .forms import UploadFileForm
from .tasks import check_file
from .models import AsyncResults


def index(request):
    if request.method == "GET":
        form = UploadFileForm()
        tasks = AsyncResults.objects.all()

        context = {
            "form": form,
            "tasks": tasks,
        }
        return render(request, "index.html", context)

    elif request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES["file"]
            filename = default_storage.save(file.name, file)

            task = AsyncResults.objects.create(
                filename=filename,
                created_at=datetime.now(),
            )
            task.save()

            check_file.delay(filename, task.id)

            messages.success(request, "Файл отправлен на проверку")
            return HttpResponseRedirect(request.path)

        messages.error(request, "Ошибка при загрузке файла")
        return HttpResponseRedirect(request.path)
    else:
        messages.error(request, "Ошибка при передаче запроса на страницу")
        return HttpResponseRedirect(request.path)
