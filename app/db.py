import os

from constans import Constans


default_db_name: str = Constans.default_db_name

def init_db() -> list[list[str]]:
    """Инициализирует бд(текстовый файл)
    Для имени файла использует дефолтное значение
    default_db_name

    Если файла нет - создает его
    
    Returns:
        contacts (list[list[str]]): Список контактов
    """
    contacts: list = []
    if os.path.exists(default_db_name):
        with open(default_db_name, 'r', encoding="utf-8") as file:
            for line in file:
                contacts.append(line.split(' | '))
    else:
       open(default_db_name, 'w', encoding="utf-8").close()
    return contacts
