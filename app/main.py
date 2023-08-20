from phonebook import Phonebook
from db import init_db
from prints import first_print, find_print, update_print
from exception import NotValidNumber, NotValidName


def main():
    contacts: list[list[str]] = init_db()
    phonebook: Phonebook = Phonebook(contacts)
    flag: bool = True

    while flag == True:
        num_command: str = first_print()

        if num_command == '0':
            break

        if num_command == '1':
            phonebook.show_contacts()

        elif num_command == '2':
            first_name=input('Введите имя: ')
            last_name=input('Введите фамилию: ')
            father_name=input('Введите отчество: ')
            org_name=input('Введите название организации: ')
            personal_number=input('Введите личный номер: ')
            work_number=input('Введите рабочий номер: ')
            try:
                phonebook.create_contact(
                    first_name=first_name, 
                    last_name=last_name, 
                    father_name=father_name,
                    org_name=org_name, 
                    personal_number=personal_number, 
                    work_number=work_number
                )
            except NotValidName as e:
                print(e)
            except NotValidNumber as e:
                print(e)
        
        elif num_command == '3':
            num_command: str = find_print()
            if num_command == '1':
                first_name = input('Введите имя: ')
                last_name = input('Введите фамилию: ')
                find_contacts = phonebook.find_contact(first_name=first_name, last_name=last_name)
            if num_command == '2':
                first_name = input('Введите имя: ')
                find_contacts = phonebook.find_contact(first_name=first_name)
            if num_command == '3':
                last_name = input('Введите фамилию: ')
                find_contacts = phonebook.find_contact(last_name=last_name)
            print(f'\nНайдено контактов ({len(find_contacts)}):')
            phonebook.print_contacts(find_contacts)
        
        elif num_command == '4':
            while True:
                num_command: str = find_print()
                if num_command == '1':
                    first_name = input('Введите имя: ')
                    last_name = input('Введите фамилию: ')
                    find_contacts = phonebook.find_contact(first_name=first_name, last_name=last_name)
                elif num_command == '2':
                    first_name = input('Введите имя: ')
                    find_contacts = phonebook.find_contact(first_name=first_name)
                elif num_command == '3':
                    last_name = input('Введите фамилию: ')
                    find_contacts = phonebook.find_contact(last_name=last_name)
                if not find_contacts:
                    print('\nКонтакт не найден')
                else:
                    phonebook.print_contacts(find_contacts)
                    break
            
            while True:
                num_command = input('\nВыберите контакт из найденных, и введите его порядковый номер.')
                if 1 <= int(num_command) <= len(find_contacts):
                    contact_for_update = find_contacts[int(num_command) - 1]
                    print('Вы выбрали: ')
                    phonebook.print_contacts([contact_for_update])
                    break
                else:
                    print('Некорректный номер.')
            num_command = update_print()
            if num_command == '1':
                first_name = input('Введите новое имя: ')
                contact = phonebook.update_contact(contact=contact_for_update, first_name=first_name)
            elif num_command == '2':
                last_name = input('Введите новую фамилию: ')
                contact = phonebook.update_contact(contact=contact_for_update, last_name=last_name)
            elif num_command == '3':
                father_name = input('Введите новое отчество: ')
                contact = phonebook.update_contact(contact=contact_for_update, father_name=father_name)
            elif num_command == '4':
                org_name = input('Введите новое название организации: ')
                contact = phonebook.update_contact(contact=contact_for_update, org_name=org_name)
            elif num_command == '5':
                personal_number = input('Введите новый личный номер: ')
                contact = phonebook.update_contact(contact=contact_for_update, personal_number=personal_number)
            elif num_command == '6':
                work_number = input('Введите новый рабочий номер: ')
                contact = phonebook.update_contact(contact=contact_for_update, work_number=work_number)
            print('Контакт обновлен успешно: ')
            phonebook.print_contacts([contact])

if __name__ == '__main__':
    main()