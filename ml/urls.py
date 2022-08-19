from . import views
from django.urls import path

urlpatterns = [
    path('', views.inputdata, name='inputdata'),
    path('ml_result/', views.ml_result, name='ml_result'),
]
