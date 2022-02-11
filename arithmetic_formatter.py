def arithmetic_arranger(problems, show_results=False):
    arranged_problems = ''
    top_row = ''
    bottom_row = ''
    dashes = ''
    solution = ''

    # Check if there are more than 5 problems in list
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        operand1 = problem.split()[0]
        operator = problem.split()[1]
        operand2 = problem.split()[2]

         # Check that there is only addition and/or subtraction problems
        if operator == '*' or operator == '/':
            return 'Error: Operator must be \'+\' or \'-\'.'

        # Check operands contain only digits
        if operand1.isdigit() is False or operand2.isdigit() is False:
            return 'Error: Numbers must only contain digits.'

        # Check if operands contain more than 4-digits
        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        calculation = ''
        if operator == '+':
            calculation = str(int(operand1) + int(operand2))
        else:
            calculation = str(int(operand1) - int(operand2))

        width = max(len(operand1), len(operand2)) + 2
        top = str(operand1).rjust(width)
        bottom = operator + str(operand2).rjust(width - 1)
        line = '-' * width
        calc = str(calculation).rjust(width)

        if problem != problems[-1]:
            top_row += top + '    '
            bottom_row += bottom + '    '
            dashes += line + '    '
            solution += calc + '    '
        else:
            top_row += top
            bottom_row += bottom
            dashes += line
            solution += calc 

    if show_results:
        arranged_problems = f'{top_row}\n{bottom_row}\n{dashes}\n{solution}'
    else:
        arranged_problems = top_row + '\n' + bottom_row + '\n' + dashes

    return arranged_problems

# print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40']))
# print(arithmetic_arranger(['3 + 855', '988 + 40']))
# print(arithmetic_arranger(['1 + 2', '1 - 9380']))