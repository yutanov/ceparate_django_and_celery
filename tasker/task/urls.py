from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('truncate_table/', views.truncate_table, name="truncate"),
    path('numbers_sums/', views.DataListView.as_view(), name="api"),
]
