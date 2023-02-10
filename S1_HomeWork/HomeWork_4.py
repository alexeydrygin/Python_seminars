# --Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def get_coordinate_range(quarter):
    if quarter == 1:
        x_range = (0, float('inf'))
        y_range = (0, float('inf'))
    elif quarter == 2:
        x_range = (float('-inf'), 0)
        y_range = (0, float('inf'))
    elif quarter == 3:
        x_range = (float('-inf'), 0)
        y_range = (float('-inf'), 0)
    elif quarter == 4:
        x_range = (0, float('inf'))
        y_range = (float('-inf'), 0)
    else:
        raise ValueError("Неверный ввод")

    return x_range, y_range


# Example usage
quarter = int(input("Введите номер четверти (1-4): "))
x_range, y_range = get_coordinate_range(quarter)
print("Диапазон воможных координат по X:", x_range)
print("Диапазон воможных координат по Y:", y_range)
