from data_create import *
def enter_data():
    name = enter_first_name()
    surname = enter_second_name()
    family = enter_family_name()
    number = enter_phone_number()
    address = enter_address_number()
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} {surname} {family}\n{number}\n{address}\n\n')

def print_data():
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())

def search_line():
    print('Выберите варинат поиска:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес')
    index = int(input('Введите вариант: ')) - 1
    searched = input('Введите поисковые данные: ')
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            if searched in new_item[index]:
                print(item, end="\n\n")


def change_info():
    print('Выберите что хотите изменить:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес')
    index = int(input('Введите вариант: ')) - 1
    def design(): # Эта функция просто для красоты
        if index == 0:
            return 'имени'
        elif index == 1:
            return 'фамилии'
        elif index == 2:
            return 'отчества'
        elif index == 3:
            return 'номера телефона'
        elif index == 4:
            return 'адреса'
    searched = input('Введите поисковые данные: ')
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
    changed_data = []
    for item in data:
        new_item = item.replace('\n', ' ').split()
        if searched in new_item[index]:
            print('\n' + item + '\n')
            changed = input(f'Введите измененную версию {design()}: ')
            new_item[index] = changed
            changed_data.append(f'{new_item[0]} {new_item[1]} {new_item[2]}\n{new_item[3]}\n{new_item[4]}')
        else:
            changed_data.append(item)
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n\n'.join(changed_data))


def delete_contact():
    print('По какому критерию будете искать контакт для удаления:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес')
    index = int(input('Введите вариант: ')) - 1
    searched = input('Введите поисковые данные: ')
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
    changed_data = []
    for item in data:
        new_item = item.replace('\n', ' ').split()
        if searched in new_item[index]:
            print('\n' + item + '\n')
            desicion = int(input('Вы точно хотите удалить этот контакт?\n'
                                 '1 - да\n'
                                 'любое другое число - нет\n'))
            if desicion == 1:
                continue
            else:
                changed_data.append(item)
        else:
            changed_data.append(item)
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n\n'.join(changed_data))
