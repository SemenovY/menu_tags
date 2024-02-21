from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Menu


def index(request: HttpRequest) -> HttpResponse:
    """
    Отображение главной страницы с древовидным меню.

    :param request: HttpRequest объект
    :return: HttpResponse объект с отрисованным меню
    """
    menus = Menu.objects.all()
    return render(request, "base.html", {"menus": menus})


def draw_menu(request: HttpRequest, path: str) -> HttpResponse:
    """
    Отображение меню на основе заданного пути.

    :param request: HttpRequest объект
    :param path: Путь для формирования меню
    :return: HttpResponse объект с отрисованным меню
    """
    splitted_path = path.split("/")
    assert len(splitted_path) > 0, "Draw_menu failed"
    return render(request, "base.html", {"menu_name": splitted_path[0], "menu_item": splitted_path[-1]})
