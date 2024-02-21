from django.db import models


class Menu(models.Model):
    name = models.CharField(
        'Название меню', max_length=30, unique=True)
    description = models.TextField(
        'Описание', max_length=250, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(
        'Название пункта меню', max_length=30, unique=True)
    description = models.TextField(
        'Описание', max_length=250, blank=True)
    url = models.CharField(
        verbose_name='URL-адрес',
        help_text=(
        'Этот параметр используется для указания адреса, на который '
        'следует перейти из текущего пункта меню. Если не указан, '
        'то ищем потомков данного пункта меню '
        'и автоматически создаем подменю на основе их данных.'),
        max_length=50, blank=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='menu_items')

    class Meta:
        ordering = ['id']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name
