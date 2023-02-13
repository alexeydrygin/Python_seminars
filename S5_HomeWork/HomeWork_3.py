
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# - Входные данные хранятся в отдельных текстовых файлах.

# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
# Восстановить
# Ввёл: stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"

# Этот код реализует алгоритм RLE (Run Length Encoding) для сжатия и восстановления текстовых данных, хранящихся в файлах.
# Функция compress_rle читает текстовые данные из файла input_file и применяет алгоритм RLE к этим данным. Результат сжатия записывается в файл output_file.
# Функция decompress_rle читает сжатые данные из файла input_file и восстанавливает их в исходный текстовый вид. Результат восстановления записывается в файл output_file.
# В конце примера использования вызываются функции compress_rle и decompress_rle, что приводит к сжатию данных в файле input.txt и восстановлению этих данных из файла compressed.txt. Результаты записываются в файлы compressed.txt и decompressed.txt соответственно.


def compress_rle(input_file, output_file):
    with open(input_file, "r") as f_in:
        data = f_in.read()
        print(f"Файл {input_file} загружен в RLE кодировщик")

    compressed_data = ""
    current_char = data[0]
    current_count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            current_count += 1
        else:
            compressed_data += f"{current_count}{current_char}"
            current_char = data[i]
            current_count = 1
    compressed_data += f"{current_count}{current_char}"

    with open(output_file, "w") as f_out:
        f_out.write(compressed_data)
        print(f"Файл {input_file} закодирован в файл {output_file} и сохранен.")


def decompress_rle(input_file, output_file):
    with open(input_file, "r") as f_in:
        compressed_data = f_in.read()

    data = ""
    current_count = ""
    for char in compressed_data:
        if char.isdigit():
            current_count += char
        else:
            data += char * int(current_count)
            current_count = ""

    with open(output_file, "w") as f_out:
        f_out.write(data)
        print(f"Файл {input_file} декодирован в файл {output_file} и сохранен.")


# Example usage:
compress_rle("input.txt", "compressed.txt")
decompress_rle("compressed.txt", "decompressed.txt")
