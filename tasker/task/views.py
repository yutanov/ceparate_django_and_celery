import requests
import json
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.views import APIView, Response
from .models import NumbersSum
from .forms import NumbersSumForm
from .serializers import NumbersSumSerializer

API = os.environ['API']


def index(request):
    if request.method == "GET":
        records = NumbersSum.objects.all()
        context = {
            "records": records,
        }
        return render(request, "index.html", context)

    elif request.method == "POST":
        form = NumbersSumForm(request.POST)

        if form.is_valid():
            number_one = request.POST.get("number_one")
            number_two = request.POST.get("number_two")
            response = requests.post(
                API, data={"number_one": number_one, "number_two": number_two}
            )
            if response.status_code == 201:
                messages.success(request, "Данные успешно добавлены")
                return HttpResponseRedirect(request.path)
            else:
                print("RESPONSE STATUS: ", response.status_code)
                messages.error(request, "Ошибка при передаче данных в API")
                return HttpResponseRedirect(request.path)
    else:
        messages.error("Ошибка при передаче запроса на страницу")
        return HttpResponseRedirect(request.path)


def truncate_table(request):
    NumbersSum.objects.all().delete()
    return redirect("index")


class DataListView(APIView):
    def get(self, request):
        numbers_sums = NumbersSum.objects.all()
        serializer = NumbersSumSerializer(numbers_sums, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NumbersSumSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data = json.loads(request.body)
        pk = data["id"]
        record = get_object_or_404(NumbersSum.objects.all(), pk=pk)
        serializer = NumbersSumSerializer(instance=record, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
