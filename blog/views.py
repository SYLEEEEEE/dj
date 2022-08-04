from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

class PostList(ListView):
    model = Post
    ordering= '-pk'
    # template_name = 'blog/index.html'

class PostDetail(DetailView):
    model = Post

# def single_post_page(request, pk):
#     post = Post.object.get(pk=pk)

#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post':post,
#         }
    # )
# def index(request):
#     posts = Post.objects.all()

#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts':posts,
#         }
#     )

def post_list(request):
    posts = Post.objects.all()
