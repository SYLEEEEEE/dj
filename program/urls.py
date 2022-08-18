from . import views
from django.urls import path

urlpatterns = [
    path('', views.inputdata, name='inputdata'),
    path('result/', views.result, name='result'),
]
