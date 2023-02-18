import csv
import os

PHONEBOOK_DATA = []

def load_data():
    global PHONEBOOK_DATA
    try:
        with open("phonebook.txt", encoding="utf-8") as f:
            PHONEBOOK_DATA = [line.strip().split(",") for line in f.readlines()]
    except FileNotFoundError:
        pass

def save_data():
    with open("phonebook.txt", "w", encoding="utf-8") as f:
        for contact in PHONEBOOK_DATA:
            f.write(",".join(contact) + "\n")

def add_contact(surname, name, phone_number, description):
    global PHONEBOOK_DATA
    PHONEBOOK_DATA.append([surname, name, phone_number, description])
    print("Контакт добавлен успешно.")

def view_contacts():
    print("Фамилия\t\t\tИмя\t\t\tТелефон\t\t\tПримечание")
    print("---------------------------------")
    for contact in PHONEBOOK_DATA:
        if len(contact) >= 4:
            print(f"{contact[0]}\t\t\t{contact[1]}\t\t\t{contact[2]}\t\t\t{contact[3]}")

def search_contact(surname):
    found_contacts = [contact for contact in PHONEBOOK_DATA if contact[0] == surname]
    if found_contacts:
        print(f"Фамилия\t\t\tИмя\t\t\tТелефон\t\t\tПримечание")
        print("---------------------------------")
        for contact in found_contacts:
            print(f"{contact[0]}\t\t\t{contact[1]}\t\t\t{contact[2]}\t\t\t{contact[3]}")
    else:
        print("Контакт не найден.")

def export_data(filename):
    if os.path.exists(filename):
        print("Файл уже существует. Пожалуйста, выберите другое имя файла.")
        return

    try:
        with open(filename, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(PHONEBOOK_DATA)
        print("Данные успешно экспортированы.")
    except IOError:
        print("Ошибка записи в файл.")

def import_data(filename):
    if not os.path.exists(filename):
        print("Файл не найден. Пожалуйста, проверьте имя файла.")
        return

    try:
        global PHONEBOOK_DATA
        with open(filename, "r") as f:
            reader = csv.reader(f)
            PHONEBOOK_DATA = [row for row in reader]
        print("Данные успешно импортированы.")
    except IOError:
        print("Ошибка чтения файла.")

