# ptmk_test

## Установка и запуск
### Запуск
Склонируйте репозиторий и перейдите в директорию проекта.

Создайте и активируйте виртуальное окружение:
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

Установите зависимости:
```sh
pip install -r requirements.txt
```
Запустите docker-контейнер:
```sh
docker-compose up -d
```

### Режим 1. Создание таблицы
```sh
python main.py 1
```

### Режим 2. Добавить одного сотрудника
```sh
python main.py 2 "Ivanov Petr Sergeevich" 2009-07-12 male
```
Формат ввода даты рождения (YYYY-MM-DD).

### Режим 3. Вывести всех сотрудников с уникальным значением ФИО + дата рождения
```sh
python main.py 3
```

### Режим 4. Массово сгенерировать и добавить сотрудников в бд
```sh
python main.py 4
```

### Режим 5. Выбрать по критериям: Пол - Мужской, ФИО - Начинается с "F"
```sh
python main.py 5
```

### Режим 6. Оптимизация запроса путем добавления индекса
```sh
python main.py 6
```