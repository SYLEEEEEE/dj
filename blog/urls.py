from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view()),#blog/ 뒤에 아무것도 없으면 포스트리스트로
    path('<int:pk>/', views.PostDetail.as_view()),#뒤에 숫자가 달리면 해당 포스트디테일로
    # path('<int:pk>/', views.single_post_page),
    # path('', views.index),
]
