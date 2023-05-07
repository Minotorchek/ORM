from django.contrib import admin
from .models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  # автоматически формируем slug по полю name

    # требуется дооформить класс, пока сделано только формирование slug
