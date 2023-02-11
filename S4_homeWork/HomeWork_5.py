# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Файл1: 2*x^2 + 4*x + 5
# Файл2: 41*x^3 + 6*x^2 + 2*x + 98
# Вывод Файл3: 41*x^3 + 8*x^2 + 6*x + 103

# работает неккорректно, не понимаю почему(.
# Если добавить в начало второго файла 41*x^3, то будет абракадабра.
# Косяк в этой функции: add_polynomials(p1, p2)

def parse_polynomial(line):
    terms = line.split(" + ")
    result = []
    for term in terms:
        if "x^" in term:
            coef, power = term.split("*x^")
            power = int(power)
        elif "x" in term:
            coef, power = term.split("*x")
            power = 1
        else:
            coef = term
            power = 0
        result.append((int(coef), power))
    return result


def add_polynomials(p1, p2):
    result = []
    i, j = 0, 0
    while i < len(p1) and j < len(p2):
        if p1[i][1] < p2[j][1]:
            result.append(p1[i])
            i += 1
        elif p1[i][1] > p2[j][1]:
            result.append(p2[j])
            j += 1
        else:
            coef = p1[i][0] + p2[j][0]
            if coef != 0:
                result.append((coef, p1[i][1]))
            i += 1
            j += 1
    result.extend(p1[i:] + p2[j:])
    return result


# Where p1 and p2 are the lists of terms representing the polynomials to be added. Each term is a tuple of the form(coefficient, power), and the terms are sorted in descending order of power. The function returns the result polynomial, represented as a list of terms in the same format.


def format_polynomial(polynomial):
    terms = []
    for coef, power in polynomial:
        if power == 0:
            terms.append(f"{coef}")
        elif power == 1:
            terms.append(f"{coef}*x")
        else:
            terms.append(f"{coef}*x^{power}")
    return " + ".join(terms)


with open("HomeWork_5_file1.txt") as file1, open("HomeWork_5_file2.txt") as file2, open("HomeWork_5_file3.txt", "w") as file3:
    line1 = file1.read().strip()
    line2 = file2.read().strip()
    polynomial1 = parse_polynomial(line1)
    polynomial2 = parse_polynomial(line2)
    result = add_polynomials(polynomial1, polynomial2)
    result_str = format_polynomial(result)
    file3.write(result_str)
    print(result_str)
