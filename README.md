README.md

# Django Project Setup

Этот документ содержит подробные инструкции по установке и запуску Django проекта.

## Требования

- Python 3.x
- Django 3.x или выше
- Виртуальное окружение (рекомендуется)

## Установка

### 1. Клонирование репозитория

```bash
git clone <URL_ВАШЕГО_РЕПОЗИТОРИЯ>
cd <ИМЯ_ВАШЕГО_ПРОЕКТА>
```

### 2. Создание виртуального окружения

Создайте виртуальное окружение для изоляции зависимостей проекта:

```bash
python -m venv venv
```

### 3. Активация виртуального окружения

- Для Windows:

```bash
venv\Scripts\activate
```

- Для macOS и Linux:

```bash
source venv/bin/activate
```

### 4. Установка зависимостей

Установите все необходимые библиотеки, указанные в `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Создание и настройка базы данных

Примените миграции для создания базы данных:

```bash
python manage.py migrate
```

### 6. Создание суперпользователя

Создайте суперпользователя для доступа к административной панели:

```bash
python manage.py createsuperuser
```

### 7. Запуск сервера разработки

Запустите сервер разработки Django:

```bash
python manage.py runserver
```

### 8. Настройка статических и медиа файлов

В настройках вашего проекта (`settings.py`) добавьте следующие строки для работы со статическими и медиа файлами:

```python
import os

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Media files (Uploaded by users)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

В файле `urls.py` вашего проекта добавьте:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ваши другие маршруты
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Структура проекта

- `manage.py`: основной скрипт для управления проектом.
- `<ИМЯ_ПРИЛОЖЕНИЯ>/`: директория вашего приложения.
  - `models.py`: содержит описание моделей.
  - `views.py`: содержит функции представления.
  - `urls.py`: маршруты приложения.
  - `templates/`: содержит HTML шаблоны.
  - `static/`: содержит статические файлы (CSS, JavaScript, изображения).
  - `admin.py`: регистрация моделей для административной панели.
- `media/`: директория для хранения загружаемых пользователями файлов.

## Дополнительные инструкции

### Использование шаблонов

Шаблон `layout.html` используется для создания общих частей страницы (например, хедера и футера). Пример использования:

```html
{% extends "layout.html" %}

{% block content %}
  <!-- Ваш контент -->
{% endblock %}
```

### Перебор элементов в шаблоне

Пример использования цикла `for` для перебора элементов в `index.html`:

```html
{% for item in items %}
  <p>{{ item.name }}</p>
{% endfor %}
```

### Динамическое отображение изображений

Для отображения изображений из папки `media` в шаблоне:

```html
<img src="{{ item.image.url }}" alt="{{ item.name }}">
```

## Завершение

Теперь ваш проект настроен и готов к запуску. Для доступа к административной панели перейдите по адресу `http://127.0.0.1:8000/admin/` и войдите с использованием созданного суперпользователя.

