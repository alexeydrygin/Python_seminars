# --(!!!Доп!!!) Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# (0,0,0), (0,0,1) и тд.
def check_equivalence(x, y, z):
    return not (x or y or z) == (not x and not y and not z)


for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            if check_equivalence(x, y, z):
                print(f"({x}, {y}, {z}) Утверждение истинно")
            else:
                print(f"({x}, {y}, {z}) Утверждение не истинно")
