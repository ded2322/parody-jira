# API для управления списком задач
Урощенная версия

# Описание
API предоставляет следующие возможности:
- Создание новой задачи. Uri: /tasks/all
- Получение списка задач. Uri: /tasks/found
- Получение информации о задаче. Uri: /tasks/add
- Обновление информации о задаче. Uri: /tasks/update
- Удаление задачи. Uri: /tasks/delete

# Что можно сделать
- Создать задачу, задать ей приоритетность от 1 до 5, добавлять описание, сроки выполнения
- Редактировать задачу (название, приоритетность, описание, сроки выполнения)
- Удалить задачу
 
# Что использовалось
Язык: Python

Фреймворк: FastApi

База данных: Postgres

Миграции: Alembic

ORM: SqlAlchemy

Тестирование: Pyttest

Документация: Swagger

# Как запустить
### С Docker-compose
1. Перейти в директорию с файлом
```commandline
cd jira-minimal
``` 
2. Собрать Docker-compose образ
```commandline
docker-compose build
```
3. Запустить Docker-compose образ
```commandline
docker-compose up
```
Cсылка с документацией http://127.0.0.1:8000/docs endpoints

### Без  Docker-compose
1. Установить python 3.9+
2. Перейти в директорию с файлом
```commandline
cd jira-minimal
```
3. Установить зависимости (предварительно активировав виртуальное окружение)
```commandline
    pip install -r requirements.txt
```
4. В файле .env изменить параметры для подключения к базе данных
```commandline
HOST_DB
PORT_DB
NAME_DB
PASS_DB
USER_DB
```
5. Запустить сервер
```commandline
    uvicorn core.main:app --reload --port 8080
```

Так-же в проекте есть логи

# Тестирование
Для тестирования необходимо иметь подключение к базе данных.
Прописать команду
```commandline
pytest -v
```
# Строение файлов и архитектура
В проекте используется луковая архитектура
### Структура проекта

- core - ядро проекта
  -  [endpoint](core%2Fendpoint)
      - [router.py](core%2Fendpoint%2Frouter.py)  - Содержится код с endpoints
      - [dependencies.py](core%2Fendpoint%2Fdependencies.py) - Содержит код с созданием экземпляра класса TasksService в котором содержится логика для endpoints 
  - [migrations](core%2Fmigrations) - Для миграции
  - [model](core%2Fmodel) - Файлы для создания моделей в базе данных 
  - [repositories](core%2Frepositories) - Создание экземпляра SqlalchemyRepository
  - [schemas](core%2Fschemas) - Схемы для валидации
  - [services](core%2Fservices) - DAO для endpoints
  - [tests](core%2Ftests) - Тесты
  - [utils](core%2Futils) - Содержит абстрактный репозитрий и его реализацию для sqlalchemy
  - [main.py](core%2Fmain.py) - Экземпляр fastapi и подключение endpoints
 
