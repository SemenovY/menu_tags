from typing import List, Optional, Union

from django import template
from django.core.exceptions import ObjectDoesNotExist

from api.models import MenuItem

register = template.Library()


@register.inclusion_tag("menu.html")
def draw_menu(menu_name: str = None, menu_item: str = None) -> dict:
    """
    Inclusion tag для отрисовки меню на основе заданных параметров.

    :param menu_name: Название меню
    :param menu_item: Название текущего активного пункта меню
    :return: Словарь с данными для отрисовки меню
    """

    def get_menu(
        menu_item: Optional[str] = None, submenu: Optional[List[Union[MenuItem, List]]] = None
    ) -> List[Union[MenuItem, List]]:
        """
        Рекурсивная функция для построения структуры меню.

        :param menu_item: Название текущего активного пункта меню
        :param submenu: Подменю текущего пункта меню
        :return: Список с пунктами меню и подменю
        """
        menu = list(items.filter(parent=None)) if menu_item is None else list(items.filter(parent__name=menu_item))
        try:
            menu.insert(menu.index(submenu[0].parent) + 1, submenu)
        except (IndexError, TypeError):
            pass
        try:
            return get_menu(items.get(name=menu_item).parent.name, menu)
        except AttributeError:
            return get_menu(submenu=submenu)
        except ObjectDoesNotExist:
            return menu

    items = MenuItem.objects.filter(menu__name=menu_name)
    return {"menu": get_menu()} if menu_name == menu_item else {"menu": get_menu(menu_item)}
