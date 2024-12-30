from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

from .models import Category, Post


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"

    def get_object(self):
        return Post.published.all()[:settings.POSTS_ON_PAGE]

class CategoryPostView(DetailView):
    model = Post
    template_name = "blog/category.html"
    context_object_name = "post_list"

    def get_queryset(self):
        # Получаем категорию по slug и проверяем, что она опубликована
        self.category = get_object_or_404(
            Category, 
            slug=self.kwargs['category_slug'], 
            is_published=True
        )
        # Возвращаем опубликованные посты в данной категории
        return self.category.posts(manager='published').all()

    def get_context_data(self, **kwargs):
        # Добавляем категорию в контекст для использования в шаблоне
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

def post_detail(request, id):
    template = "blog/detail.html"
    post = get_object_or_404(Post.published, id=id)
    context = {"post": post}
    return render(request, template, context)
