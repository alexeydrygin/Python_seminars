import csv

PHONEBOOK_DATA = []

def load_data():
    global PHONEBOOK_DATA
    try:
        with open("phonebook.txt") as f:
            PHONEBOOK_DATA = [line.strip().split(",") for line in f.readlines()]
    except FileNotFoundError:
        pass

def save_data():
    with open("phonebook.txt", "w") as f:
        for contact in PHONEBOOK_DATA:
            f.write(",".join(contact) + "\n")

def add_contact(name, phone_number):
    global PHONEBOOK_DATA
    PHONEBOOK_DATA.append([name, phone_number])
    print("Контакт добавлен успешно.")

def view_contacts():
    print("Name\t\tPhone number")
    print("---------------------------------")
    for contact in PHONEBOOK_DATA:
        print(f"{contact[0]}\t\t{contact[1]}")

def search_contact(name):
    found_contacts = [contact for contact in PHONEBOOK_DATA if contact[0] == name]
    if found_contacts:
        print(f"Name\t\tPhone number")
        print("---------------------------------")
        for contact in found_contacts:
            print(f"{contact[0]}\t\t{contact[1]}")
    else:
        print("Контакт не найден.")

def export_data(filename):
    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerows(PHONEBOOK_DATA)
    print("Данные успешно экспортированы.")

def import_data(filename):
    global PHONEBOOK_DATA
    with open(filename, "r") as f:
        reader = csv.reader(f)
        PHONEBOOK_DATA = [row for row in reader]
    print("Данные успешно импортированы.")
