from django.contrib import admin

from .models import Category, Location, Post

admin.site.register(Location)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "slug",
        "is_published",
        "created_at",
    )
    list_editable = ("slug", "description")
    search_fields = ("title",)
    list_display_links = ("title",)
