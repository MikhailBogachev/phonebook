from constans import Constans
from validators import validate_name, validate_phone_number
from exception import NotValidName, NotValidNumber


class Phonebook:
    default_db_name: str = Constans.default_db_name
    pagination_num: int = Constans.pagination_num

    def __init__(self, db: list[list[str]]) -> None:
        self.db: list[list[str]] = db
    
    def _rewrite_in_file(self) -> None:
        """
        Перезаписывает файл на основе актуального self.db
        """
        file = open(self.default_db_name, 'w', encoding="utf-8")
        for line in self.db:
            file.write(' | '.join(line).replace('\n', '') + '\n')
        file.close()

    def _write_in_file(self, contact: list[str]) -> None:
        """
        Записывает новый контакт в файл
        """
        file = open(self.default_db_name, 'a', encoding="utf-8")
        file.write(' | '.join(contact) + '\n')
        file.close()
    
    def print_contacts(self, data: list[list[str]]) -> None:
        """
        Выводит контакт
        """
        for ind, line in enumerate(data):
            print(f'{ind+1}. ', ' | '.join(line))

    def show_contacts(self) -> None:
        """
        Выводит все контакты в постраничном виде
        """
        if not self.db:
            print('\nКонтактов еще нет')
            return
        print()
        i = 1
        while i <= len(self.db) // self.pagination_num + 1:
            for ind, line in enumerate(
                self.db[
                    (i-1) * self.pagination_num: i * self.pagination_num
                ]
            ):
                print(f'{ind + 1}. ', ' | '.join(line))
            print(f'Страница {i}')
            if ind + 1 < self.pagination_num or i * self.pagination_num >= len(self.db):
            #if (ind + 1 + self.pagination_num) * i >= len(self.db) - 1:
                break
            n = input('Введите:\n1 - для перехода на следующую страницу\n'
                      '0 - для выхода в главное меню\n')
            if n == '0':
                break
            elif n == '1':
                i += 1

    def create_contact(
        self,
        first_name: str,
        personal_number: str,
        last_name: str,
        father_name: str,
        org_name: str,
        work_number: str
    ) -> None:
        """
        Функция для создания контакта

        Args:
            first_name (str): Имя
            personal_number (str): Личный номер
            last_name (str): Фамилия
            father_name (str): Отчество
            org_name (str): Название организации
            work_number (str): Рабочий номер
        """
        data = [first_name, last_name, father_name, 
                org_name, personal_number, work_number]
        if not all(map(validate_name, data[:4])):
            raise NotValidName('Проверьте правильность вводимых имен/названий')
        if not all(map(validate_phone_number, data[4:])):
            raise NotValidNumber('Проверьте правильность вводимых номеров телефонов')
        self.db.append(data)
        self._write_in_file(data)
    
    def find_contact(
        self,
        first_name: str | None = None,
        last_name: str | None = None
    ) -> list[list[str]]:
        """
        Выполянет поиск контакта по имени и/или фамилии

        Args:
            first_name (str | None): Имя
            last_name (str | None): Фамилия
        Returns:
            find_result (list[list[str]]): Список найденных контактов
        """
        find_result: list[str] = []
        for row in self.db:
            if first_name and last_name:
                if first_name == row[0] and last_name == row[1]:
                    find_result.append(row)
            elif first_name and first_name == row[0]:
                find_result.append(row)
            elif last_name and last_name == row[1]:
                find_result.append(row)
        return find_result
    
    def update_contact(
        self,
        contact: list[str],
        first_name: str | None  = None,
        last_name: str | None  = None,
        father_name: str | None  = None,
        org_name: str | None  = None,
        personal_number: str | None  = None,
        work_number: str | None  = None
    ) -> list[str]:
        """
        Обновляет контак.

        Args:
            contact (list[str]): Контакт, к-й необходимо обновить.
            first_name (str | None): Новое имя.
            last_name (str | None): Новая фамилия.
            father_name (str | None): Новое отчество.
            org_name (str | None): Новое название организации.
            personal_number (str | None): Новый личный номер.
            work_number (str | None): Новый рабочий номер.
        Returns:
            new_contact (list[str]): Обновленный контакт
        """
        for ind, row in enumerate(self.db):
            if contact == row:
                index_contact = ind
                break
        if first_name:
            self.db[index_contact][0] = first_name
        elif last_name:
            self.db[index_contact][1] = last_name
        elif father_name:
            self.db[index_contact][2] = father_name
        elif org_name:
            self.db[index_contact][3] = org_name
        elif personal_number:
            self.db[index_contact][4] = personal_number
        elif work_number:
            self.db[index_contact][5] = work_number + '\n'
        self._rewrite_in_file()
        new_contact: list[str] = self.db[index_contact]
        return new_contact
