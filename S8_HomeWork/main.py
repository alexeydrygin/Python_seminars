import login
import teacher
import student

def main():
    # запрашиваем логин и пароль
    username, password = login.get_credentials()

    # проверяем логин и пароль
    user_type = login.check_credentials(username, password)

    # запускаем нужный модуль
    if user_type == 'teacher':
        teacher.run()
    elif user_type == 'student':
        student.run()
    else:
        print('Неверный логин или пароль')

if __name__ == '__main__':
    main()
