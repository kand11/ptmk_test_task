import time
import mysql.connector
from pathlib import Path
from employee import Employee


class Database:
    """Класс Database для взаимодействия с базой данных."""

    def __init__(self) -> None:
        """Инициализация подключения к базе данных."""
        self.config = {
            "host": "localhost",
            "port": 3307,
            "user": "user",
            "password": "password",
            "database": "ptmk_db"
        }
        self.conn = mysql.connector.connect(**self.config)
        self.cursor = self.conn.cursor(buffered=True, dictionary=True)

    def close(self) -> None:
        """Закрытие соединения с базой данных."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    @staticmethod
    def load_sql(filename: str) -> str:
        """
        Загружает SQL из папки sql.
        :return:
        """
        sql_path = Path(__file__).parent / "sql_scripts" / filename
        with open(sql_path, "r", encoding="utf-8") as f:
            return f.read()

    def create_table(self) -> None:
        """Создание таблицы сотрудников (employees), если ее нет."""
        query = self.load_sql("create_table.sql")
        self.cursor.execute(query)
        self.conn.commit()
        print("Таблица сотрудников создана или уже существует.")

    def insert_employee(self, full_name: str, birth_date, sex: str) -> None:
        """
        Вставка информации о сотруднике в базу данных.
        :param full_name: ФИО сотрудника.
        :param birth_date: Дата рождения сотрудника (YYYY-MM-DD).
        :param sex: Пол сотрудника.
        """
        query = self.load_sql("insert_employees.sql")
        self.cursor.execute(query, (full_name, birth_date, sex))
        self.conn.commit()
        print(f"Сотрудник {full_name} добавлен в базу.")

    def print_all(self) -> None:
        """Вывод всех строк справочника с уникальным значением ФИО + дата рождения."""
        query = self.load_sql("select_employees.sql")
        self.cursor.execute(query)

        for i in self.cursor.fetchall():
            emp = Employee(i['full_name'], i['birth_date'].strftime('%Y-%m-%d'), i['sex'])
            emp_age = emp.age(emp.birth_date)
            emp.get_data(emp_age)

    def insert_list_employees(self, data: list[str, str, str]) -> None:
        """
        Вставка массива строк о сотрудниках в базу данных.
        :param data: массив данных о сотрудниках
        """
        query = self.load_sql("insert_employees.sql")
        self.cursor.executemany(query, data)
        self.conn.commit()
        print(f"Добавлено {len(data)} сотрудников в базу.")

    def select_f_male(self) -> None:
        """Выводит результат выборки по критериям: Пол - Мужской, ФИО - Начинается с "F"."""
        query = self.load_sql("select_f_male_employees.sql")
        start = time.time()
        self.cursor.execute(query)
        end = time.time()
        result = self.cursor.fetchall()
        print(f"Найдено: {len(result)} строк за {end-start} сек")

    def optimize(self) -> None:
        """Создает индекс для оптимизации времени выборки."""
        try:
            query = self.load_sql("show_index.sql")
            self.cursor.execute(query)
            if not self.cursor.fetchone():
                query = self.load_sql("create_index.sql")
                self.cursor.execute(query)
                print("Индекс создан.")
            else:
                print("Индекс уже существует")
        except Exception as e:
            print(f"Ошибка при создании индекса: {e}")
