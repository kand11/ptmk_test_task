"""
constants.py
------------
Содержит константы и справочные данные, используемые в проекте:
 - количество сгенерированных строк сотрудников;
 - количество обязательных сгенерированных строк сотрудников;
 - списки фамилий, имён и отчеств;
 - распределение по полу.
"""

COUNT_EMPLOYEES = 1000000

COUNT_F_MALE_EMPLOYEES = 100

# =========================
#  Фамилии (по алфавиту)
# =========================
SURNAMES = {
    1: {"Adamyan", "Arutyunyan", "Avanesyan"},         # A
    2: {"Babayan", "Bagdasaryan", "Barseghyan"},       # B
    3: {"Chernenko", "Chumachenko", "Chubenko"},       # C
    4: {"Davtyan", "Danielyan", "Dzhanyan"},           # D
    5: {"Egiazaryan", "Esayan", "Erzinkyan"},          # E
    6: {"Filipchuk", "Fedorchuk", "Filenko"},          # F
    7: {"Grigoryan", "Gasparyan", "Galstyan"},         # G
    8: {"Harutyunyan", "Hakobyan", "Hambardzumyan"},   # H
    9: {"Ivashko", "Isayan", "Israelyan"},             # I
    10: {"Janibekyan", "Jaloyan", "Javakhishvili"},    # J
    11: {"Kovalenko", "Kirakosyan", "Kostyuchenko"},   # K
    12: {"Lukashenko", "Levonyan", "Lazaryan"},        # L
    13: {"Manukyan", "Melkonyan", "Melnik"},           # M
    14: {"Nazaryan", "Nikonenko", "Nalbandyan"},       # N
    15: {"Oganesyan", "Ohanyan", "Ordyan"},            # O
    16: {"Petrosyan", "Pogosyan", "Panchenko"},        # P
    17: {"Rostomyan", "Romanenko", "Rafayelyan"},      # R
    18: {"Savchenko", "Sargsyan", "Stepanyan"},        # S
    19: {"Tkachenko", "Tadevosyan", "Tumanyan"},       # T
    20: {"Ustimenko", "Ushchenko", "Ushanenko"},       # U
    21: {"Vardanyan", "Voskanyan", "Vasylenko"},       # V
    22: {"Yevtushenko", "Yeranosyan", "Yepiskopyan"},  # Y
    23: {"Zakharchenko", "Zakaryan", "Zograbyan"}      # Z
}

# =========================
#  Мужские имена
# =========================
MALE_NAMES = {
    "Ivan", "Sergey", "Dmitry", "Alexey", "Nikita",
    "Egor", "Kirill", "Andrey", "Mikhail", "Roman"
}

# =========================
#  Женские имена
# =========================
FEMALE_NAMES = {
    "Anna", "Maria", "Olga", "Elena", "Anastasia",
    "Daria", "Sofia", "Polina", "Veronika", "Ekaterina"
}

# =========================
#  Отчества (мужские)
# =========================
MALE_PATRONYMICS = {
    "Ivanovich", "Sergeevich", "Dmitrievich", "Alexeevich", "Nikolaevich",
    "Andreevich", "Petrovich", "Mikhailovich", "Pavlovich", "Vladimirovich"
}

# =========================
#  Отчества (женские)
# =========================
FEMALE_PATRONYMICS = {
    "Ivanovna", "Sergeevna", "Dmitrievna", "Alexeevna", "Nikolaevna",
    "Andreevna", "Petrovna", "Mikhailovna", "Pavlovna", "Vladimirovna"
}
