def first_print():
    print('')
    print('\nДоступные команды:')
    print('1. Показать все контакты.')
    print('2. Добавить новый контакт.')
    print('3. Найти контакт')
    print('4. Изменить контакт.')
    print('0. Выйти из телефонной книги.')
    num_command = input('Выберите номер команды: ')
    return num_command

def find_print():
    print('\nПоиск доступен по имени и/или фамилии. \nВыберите параметры поиска:')
    print('1. Поиск по имени и фамилии.')
    print('2. Поиск по имени.')
    print('3. Поиск по фамилии.')
    num_command = input('Выберите номер команды: ')
    return num_command

def update_print():
    print('Что меняем?')
    print('1. Имя.')
    print('2. Фамилия.')
    print('3. Отчество.')
    print('4. Название организации.')
    print('5. Личный номер.')
    print('6. Рабочий номер.')
    num_command = input('Выберите номер команды: ')
    return num_command
