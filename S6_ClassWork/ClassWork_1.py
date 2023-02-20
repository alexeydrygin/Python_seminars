# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +, -, /, *.
# Приоритет операций стандартный.


def evaluate_expression(expression):
    # Remove whitespaces
    expression = expression.replace(" ", "")

    # Check if the expression is just a number
    if expression.isdigit():
        return int(expression)

    # Split the expression into sub-expressions
    sub_expressions = []
    current_sub_expression = ""
    in_sub_expression = False
    for char in expression:
        if char == "(":
            in_sub_expression = True
        elif char == ")":
            in_sub_expression = False
            sub_expressions.append(current_sub_expression)
            current_sub_expression = ""
        elif in_sub_expression:
            current_sub_expression += char
        else:
            sub_expressions.append(char)

    # Evaluate sub-expressions recursively
    i = 0
    while i < len(sub_expressions):
        sub_expression = sub_expressions[i]
        if sub_expression in ["+", "-", "*", "/"]:
            operator = sub_expression
            left_operand = evaluate_expression(sub_expressions[i - 1])
            right_operand = evaluate_expression(sub_expressions[i + 1])
            if operator == "+":
                result = left_operand + right_operand
            elif operator == "-":
                result = left_operand - right_operand
            elif operator == "*":
                result = left_operand * right_operand
            elif operator == "/":
                result = left_operand / right_operand
            sub_expressions = sub_expressions[:i -
                                              1] + [result] + sub_expressions[i + 2:]
            i = 0
        else:
            i += 1

    return sub_expressions[0]


expression = input("Enter the expression: ")
result = evaluate_expression(expression)
print(result)
