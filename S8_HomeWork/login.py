def get_credentials():
    # запрашиваем логин и пароль
    username = input('Логин: ')
    password = input('Пароль: ')
    return username, password

def check_credentials(username, password):
    # проверяем логин и пароль
    with open('users.txt', 'r') as f:
        for line in f:
            user, passwd, user_type = line.strip().split(':')
            if username == user and password == passwd:
                return user_type
    return None
