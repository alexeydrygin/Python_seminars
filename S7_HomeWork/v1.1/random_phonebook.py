import random

# Списки с данными для генерации случайных пользователей
surnames = ["Иванов", "Петров", "Сидоров", "Рыков", "Смирнов", "Васин", "Козлов", "Новиков"]
names = ["Иван", "Петр", "Сидор", "Алексей", "Максим", "Дмитрий", "Андрей", "Константин"]
phone_formats = ["+7-###-###-##-##", "+7 (###) ###-##-##", "+7 ### ###-##-##"]
notes = ["Работа", "Друзья", "Семья", "Другое"]

# Открываем файл для записи
with open("phonebook.txt", "w", encoding="utf-8") as f:
    # Генерируем данные для 30 пользователей и записываем их в файл
    for i in range(30):
        surname = random.choice(surnames)
        name = random.choice(names)
        phone_number = random.choice(phone_formats).replace("#", str(random.randint(0, 9)))
        note = random.choice(notes)
        f.write(f"{surname},{name},{phone_number},{note}\n")
print('Файл успешно создан.')