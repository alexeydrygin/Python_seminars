import phonebook

def main():
    phonebook.load_data()
    while True:
        print("Добро пожаловать в телефонный справочник!")
        print("1. Добавить контакт")
        print("2. Просмотр контакта")
        print("3. Поиск контакта")
        print("4. Экспорт данных")
        print("5. Импорт данных")
        print("6. Выход")
        choice = input("Введите ваш выбор: ")
        if choice == "1":
            surname = input('Введите фамилию: ')
            name = input('Введите имя: ')
            phone_number = input('Введите телефон: ')
            description = input('Введите описание: ')
            phonebook.add_contact(surname, name, phone_number, description)
        elif choice == "2":
            phonebook.view_contacts()
        elif choice == "3":
            surname = input("Введите фамилию: ")
            phonebook.search_contact(surname)
        elif choice == "4":
            filename = input("Введите имя файла: ")
            phonebook.export_data(filename)
        elif choice == "5":
            filename = input("Введите имя файла: ")
            phonebook.import_data(filename)
        elif choice == "6":
            phonebook.save_data()
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")

if __name__ == "__main__":
    main()
