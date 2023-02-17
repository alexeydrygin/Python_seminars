import digit, in_num, log

def button_click():
    print('Введите "0" если хотите продолжить')
    print('Введите "1" если хотите закончить')
    flag = int(input())
    while flag == 0:
        primer = digit.parse()
        result = digit.calculate(primer)
        in_num.viev_data(result)
        log.loger(primer, result)
        print('Введите "0" если хотите продолжить')
        print('Введите "1" если хотите закончить')
        flag = int(input())
    print('Программа завершена.')