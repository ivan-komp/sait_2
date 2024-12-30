from django.urls import path

from . import views
from .views import IndexView, CategoryPostView

app_name = "blog"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:id>/", views.post_detail, name="post_detail"),
    path(
        "category/<slug:category_slug>/",
        CategoryPostView.as_view(),
        name="category_posts",
    ),
]
