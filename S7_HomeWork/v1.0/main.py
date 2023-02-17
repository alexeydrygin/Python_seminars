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
            name = input("Введите имя: ")
            phone_number = input("Введите номер телефона: ")
            phonebook.add_contact(name, phone_number)
        elif choice == "2":
            phonebook.view_contacts()
        elif choice == "3":
            name = input("Введите имя: ")
            phonebook.search_contact(name)
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
