from django.contrib import admin
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass

@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass