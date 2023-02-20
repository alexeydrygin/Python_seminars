import database

def run():
    while True:
        print('1 - Добавить ученика')
        print('2 - Удалить ученика')
        print('3 - Добавить оценку')
        print('4 - Выйти')

        choice = input('Выберите действие: ')
        if choice == '1':
            name = input('Введите имя: ')
            surname = input('Введите фамилию: ')
            patronymic = input('Введите отчество: ')
            birthdate = input('Введите дату рождения: ')
            klass = input('Введите класс: ')
            address = input('Введите адрес: ')
            phone = input('Введите телефон: ')
            database.add_student(name, surname, patronymic, birthdate, klass, address, phone)
        elif choice == '2':
            surname = input('Введите фамилию удаляемого ученика: ')
            database.delete_student(surname)
        elif choice == '3':
            surname = input('Введите фамилию ученика: ')
            subject = input('Введите предмет: ')
            grade = input('Введите оценку: ')
            database.add_grade(surname, subject, grade)
        elif choice == '4':
            break
        else:
            print('Неверный выбор')

if __name__ == '__main__':
    run()
