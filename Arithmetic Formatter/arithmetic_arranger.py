def arithmetic_arranger(problems, val=False):
    # Error if it contains more than five problems
    if len(problems) > 5:
        return "Error: Too many problems."

    for i, problem in enumerate(problems):
        # split each problem in values and operator-symbol
        val1, operator, val2 = problem.split()

        # check if its only + or - operator
        if operator is  ("*" or "/"):
            return "Error: Operator must be '+' or '-'."
        # if values contains anything els than digits raise an Error
        elif (val1.isdigit() and val2.isdigit()) is False:
            return "Error: Numbers must only contain digits."
        # raise Error by values that are longer four digits
        elif (len(val1) or len(val2)) > 4:
            return "Error: Numbers cannot be more than four digits."

    # list of all operations in str format
    operations = list(map(lambda x: x.split()[1], problems))

    numbers = []  # list of all operands in str format
    for i in problems:
        p = i.split()
        numbers.extend([p[0], p[2]])

    top_row = ''
    dashes = ''
    values = list(map(lambda x: eval(x), problems))
    solutions = ''
    for i in range(0, len(numbers), 2):
        space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2
        top_row += numbers[i].rjust(space_width)
        dashes += '-' * space_width
        solutions += str(values[i // 2]).rjust(space_width)
        if i != len(numbers) - 2:
            top_row += ' ' * 4
            dashes += ' ' * 4
            solutions += ' ' * 4

    bottom_row = ''
    for i in range(1, len(numbers), 2):
        space_width = max(len(numbers[i - 1]), len(numbers[i])) + 1
        bottom_row += operations[i // 2]
        bottom_row += numbers[i].rjust(space_width)
        if i != len(numbers) - 1:
            bottom_row += ' ' * 4

    if val:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes, solutions))
    else:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes))
    return arranged_problems