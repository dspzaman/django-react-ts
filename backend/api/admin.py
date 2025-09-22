from django.contrib import admin
from .models import Task, Category, Product

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'completed', 'created']
    list_filter = ['completed', 'created']
    search_fields = ['title']
    list_editable = ['completed']
    ordering_Desc = ['-created']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "productName", "price", "category")
    list_filter = ("category",)