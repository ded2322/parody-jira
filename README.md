# Todo
Этот проект позволяет развернуть с помощью Docker, backend-api для todo листа

Улучшеная версия с поддержкой docker: https://github.com/ded2322/parody-jira/tree/main


## Функциональность
- Создание задачи (Название,описание, состояние(состояние можно создать отдельно и присвоить специальное название))
- Просмотр задач (Отдает в виде json)
- Добавление состояния задач
- Просмотр состояния задач
- Удалить задачу/состояние

## Использование
1. Убедитесь, что у вас установлен Python версии 3.12.
2. Установите необходимые зависимости, выполнив команду: `pip install -r requirements.txt`.
3. Скачать pgpostgres, создать сервер
4. Изменить данные в .env файле

## Стиль кода

Проект следует стандартам стиля кода PEP 8. Для проверки и автоматического форматирования кода используются следующие инструменты:

- Flake8: Линтер для проверки стиля кода и выявления потенциальных ошибок.
- Black: Автоматический форматтер кода, обеспечивающий единообразие стиля во всем проекте.

----
Надеюсь, этот проект будет полезен для вас! Если вам понравился проект, не забудьте поставить звездочку ⭐️ на GitHub.
