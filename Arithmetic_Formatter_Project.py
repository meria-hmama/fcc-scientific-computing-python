def arithmetic_arranger(problems, show_answers=False):
    # Too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        left, operator, right = parts

        #Operator must be + or -
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        #  Numbers must only contain digits
        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."

        # Numbers cannot be more than four digits
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        #width
        width = max(len(left), len(right)) + 2

        # Building lines
        first_line.append(left.rjust(width))
        second_line.append(operator + right.rjust(width - 1))
        dashes.append('-' * width)

        # Compute answer
        if show_answers:
            if operator == '+':
                result = str(int(left) + int(right))
            else:
                result = str(int(left) - int(right))
            answers.append(result.rjust(width))

    # 4 spaces thing 
    arranged = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dashes)
    if show_answers:
        arranged += '\n' + '    '.join(answers)

    return arranged
