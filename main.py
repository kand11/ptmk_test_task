import sys
import numpy as np
import random
from employee import Employee
from database import Database
from constants import (
    SURNAMES,
    MALE_NAMES,
    FEMALE_NAMES,
    MALE_PATRONYMICS,
    FEMALE_PATRONYMICS,
    COUNT_EMPLOYEES,
    COUNT_F_MALE_EMPLOYEES
)


def generate_employees(count: int) -> list:
    """
    Генератор списка сотрудников.
    :param count: Количество сотрудников.
    :return: employees: Сгенерированный список сотрудников.
    """
    employees = []
    surname_word_list = np.random.randint(1, 24, count)
    gender_list = np.random.choice(['male', 'female'], count, p=[0.5, 0.5])
    for i in range(count):
        surname_set = SURNAMES[int(surname_word_list[i])]
        birth_date = f"{random.randint(1995, 2005)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
        full_name = random.choice(list(surname_set))
        if gender_list[i] == 'male':
            full_name += ' ' + random.choice(list(MALE_NAMES)) + ' ' + random.choice(list(MALE_PATRONYMICS))
        else:
            full_name += ' ' + random.choice(list(FEMALE_NAMES)) + ' ' + random.choice(list(FEMALE_PATRONYMICS))
        employees.append((full_name, birth_date, str(gender_list[i])))
    return employees


def generate_f_male_employees(count: int) -> list:
    """
    Генератор списка сотрудников, у которых Пол - Мужской, ФИО - Начинается с "F".
    :param count: Количество сотрудников.
    :return: employees: Сгенерированный список сотрудников.
    """
    employees = []
    surname_set = SURNAMES[6]
    gender = 'male'

    for i in range(count):
        birth_date = f"{random.randint(1995, 2005)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}"
        full_name = random.choice(list(surname_set)) + ' ' + random.choice(list(MALE_NAMES)) + ' ' + random.choice(list(MALE_PATRONYMICS))
        employees.append((full_name, birth_date, gender))
    return employees


def main():
    """
    Основная точка входа в программу.
    Режимы:
      1 — создать таблицу
      2 — добавить одного сотрудника
      3 — вывести всех сотрудников с уникальным значением ФИО + дата рождения
      4 — массово сгенерировать и внести сотрудников
      5 — выбрать по критериям: Пол - Мужской, ФИО - Начинается с "F"
      6 — оптимизировать запрос (создать индекс)
    """
    mode = int(sys.argv[1])
    db = Database()
    match mode:
        case(1):
            db.create_table()
        case(2):
            full_name, birth_date, sex = sys.argv[2], sys.argv[3], sys.argv[4]
            emp = Employee(full_name, birth_date, sex)
            emp.insert_in_db(db)
        case(3):
            db.print_all()
        case(4):
            employee_list = generate_employees(COUNT_EMPLOYEES)
            f_male_employee_list = generate_f_male_employees(COUNT_F_MALE_EMPLOYEES)
            db.insert_list_employees(employee_list)
            db.insert_list_employees(f_male_employee_list)
        case(5):
            db.select_f_male()
        case(6):
            db.optimize()
            print("Проверка запроса после оптимизации:")
            db.select_f_male()
    db.close()


if __name__ == "__main__":
    main()
