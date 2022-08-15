from . import views
from django.urls import path

urlpatterns = [
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('tag/<str:slug>/', views.tag_page),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/new_comment/', views.new_comment),
    path('', views.PostList.as_view()),#blog/ 뒤에 아무것도 없으면 포스트리스트로
    path('<int:pk>/', views.PostDetail.as_view()),#뒤에 숫자가 달리면 해당 포스트디테일로

]
