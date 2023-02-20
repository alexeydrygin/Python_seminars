# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension 
# Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]


lst = [12,'sadf',5643]

def separate_by_elements(lst):
    result = []
    result.append(list(filter(lambda i: str(i).isalpha(), lst)))
    result.append(list(filter(lambda i: str(i).isdigit(), lst)))
    return result

print(lst)
print(separate_by_elements(lst))