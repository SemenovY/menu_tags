### Тестовое задание:
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8) На отрисовку каждого меню требуется ровно 1 запрос к БД

### Технологии:

- Python
- Django
- Postgres

### Установка и запуск:
1. Клонируйте репозиторий с GitHub и введите данные для переменных окружения:
```bash
git clone https://github.com/SemenovY/menu_tags
```

2. Создайте и активируйте виртуальное окружение:
   * Linux/macOS
   ```bash
    python -m venv venv && source venv/bin/activate
   ```
   * Windows
   ```bash
    python -m venv venv && source venv/Scripts/activate
   ```

3. Установите в виртуальное окружение все необходимые зависимости из  **requirements.txt**:
```bash
python -m pip install --upgrade pip && pip install -r requirements.txt
```

4. Выполните миграции, загрузку данных:
```bash
python manage.py makemigrations && \
python manage.py migrate && \
```
5. Нужно создать суперпользователя и запустить сервер:
```bash
python manage.py createsuperuser && \
python manage.py runserver
```
Сервер запустится локально по адресу `http://127.0.0.1:8000/`

### Локальный запуск:

#### Docker Compose/PostgreSQL

1. Из корневой директории проекта выполните команду:
```bash
docker compose -f docker-compose.yml up -d --build
```
Проект будет развернут в двух docker-контейнерах (db, app) по адресу `http://127.0.0.1:8000`.

2. Остановить docker и удалить контейнеры, тома базы данных, статики и медиа можно командой из корневой директории проекта:
```bash
docker compose -f docker-compose.yml down -v
```
3. Создать суперпользователя:
```bash
docker exec -it app python manage.py createsuperuser
```
Адреса:
  - http://127.0.0.1:8000/menu/
  - http://127.0.0.1:8000/admin/

### Автор
- Семёнов Юрий -  [GitHub](https://github.com/SemenovY )
### =^..^=______/
