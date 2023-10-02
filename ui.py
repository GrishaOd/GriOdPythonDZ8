from logger import *

def interface():
    cmd = 0
    while cmd != '6':
        print('Выберите действие:\n'
              '1. Добавить контакт\n'
              '2. Вывести все контакты\n'
              '3. Поиск контакта\n'
              '4. Изменение контакта\n'
              '5. Удаление контакта\n'
              '6. Выход\n')
        cmd = input('Введите действие: ')
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            cmd = input('Введите действие: ')
        match cmd:
            case '1':
                enter_data()
            case '2':
                print_data()
            case '3':
                search_line()
            case '4':
                change_info()
            case '5':
                delete_contact()
            case '6':
                print('Всего доброго')