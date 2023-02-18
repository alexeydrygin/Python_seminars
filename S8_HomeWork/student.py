import database

def run():
    surname = input('Введите фамилию ученика: ')
    grades = database.get_grades(surname)
    if grades:
        for subject, grade in grades.items():
            print(f'{subject}: {grade}')
    else:
        print('Оценок не найдено')

if __name__ == '__main__':
    run()
