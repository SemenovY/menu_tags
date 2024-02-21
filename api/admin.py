from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Класс настроек администрирования для модели Menu.
    """

    pass


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """
    Класс настроек администрирования для модели MenuItem.
    """

    pass
