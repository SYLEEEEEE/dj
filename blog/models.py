from operator import mod
from django.db import models
from matplotlib.pyplot import title

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'no.{self.pk} {self.title}'  # 처음에 순서대로 부여된 pk가 적용됨

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'