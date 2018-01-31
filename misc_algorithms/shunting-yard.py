"""
Evaluates arithmetic expressions with support for non-integer and negative numbers
    (^ for exponentiation)
    *please be explicit with operations (do 3*(2+1) not 3(2+1))
"""

from data_structures.Stack import Stack


class InvalidInputError(Exception):
    def __init__(self, idx, element):
        self.idx=idx
        self.element=element


def parse_expr(expr):
    expr = [item for item in expr if item != ' ']


# if operator with greater precedence -> skip 1 down in values stack

    expr.append(')')
    return expr


# create parser that allows for double digit numbers & negative numbers & decimal numbers (e..g 16)


def calculate(operand, values):
    first = values.pop()
    second = values.pop()
    if operand == '^':
        values.push(second ** first)
    elif operand == '*':
        values.push(first * second)
    elif operand == '/':
        values.push(second / first)
    elif operand == '+':
        values.push(first + second)
    elif operand == '-':
        values.push(second - first)
    return values


def evaluate_expression(expr):
    values = Stack()
    operators = Stack()

    for idx, element in enumerate(expr):
        if element == '(': pass
        elif element in ['^', '+', '-', '*', '/']:
            operators.push(element)
        elif element.isdigit():
            values.push(int(element))
        elif element == ')':
            if operators.get_size() == 0: continue
            operand = operators.pop()
            values = calculate(operand, values)
        else: raise InvalidInputError(idx=idx, element=element)

    while operators.get_size() != 0:
        operand = operators.pop()
        values = calculate(operand, values)

    assert values.get_size() == 1, "Values stack contains {} elements at termination".format(values.get_size())
    return float(values.pop())


if __name__ == '__main__':
    expr = parse_expr(input('Please enter an arithmetic expression: '))
    try:
        print(evaluate_expression(expr))
    except InvalidInputError as e:
        print('Input error at element "{element}" (index {idx})'.format(idx=e.idx, element=e.element))
