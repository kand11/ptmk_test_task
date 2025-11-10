from datetime import datetime


class Employee:
    """Класс Сотрудник (Employee)"""

    def __init__(self, full_name: str, birth_date: str, sex: str) -> None:
        """
        Конструктор объекта класса.
        :param full_name: ФИО сотрудника.
        :param birth_date: Дата рождения сотрудника (YYYY-MM-DD).
        :param sex: Пол сотрудника.
        """
        self.full_name = full_name
        self.sex = sex
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    @staticmethod
    def age(birth_date: datetime) -> int:
        """
        Вычисление возраста сотрудника по его дате рождения.
        :param birth_date: Дата рождения сотрудника (YYYY-MM-DD).
        :return: employee_age: Полный возраст сотрудника в годах.
        """
        if birth_date is None:
            return 0
        today = datetime.today()
        employee_age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return employee_age

    def insert_in_db(self, db) -> None:
        """
        Добавление сотрудника в базу данных
        :param db: Экземпляр класса Database
        """
        db.insert_employee(self.full_name, self.birth_date, self.sex)

    def get_data(self, employee_age: int) -> None:
        """Выводит информацию о сотруднике в консоль."""
        print(f"{self.full_name} | {self.sex} | {self.birth_date.date()} | {employee_age} лет")
