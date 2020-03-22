import re
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def add(equation: str) -> str:
    print(equation)
    num = [int(number) for number in equation.split() if number.isdigit()]
    return str(sum(num))


def minus(equation: str) -> str:
    print(f"HERE WE BE {equation}")
    numbers = [int(number) for number in equation.split() if number.isdigit()]
    print(numbers)
    return str(numbers[0] - numbers[1])


def symbol(equation: str) -> str:
    symbols = ["-", "+"]
    sym = None
    for x in equation:
        for s in symbols:
            if x == s:
                sym = s
                break

    if sym == "-":
        print("MINUS")
        return "minus"
    if sym == "+":
        print("ADD")
        return "add"


def do_math(equation: str) -> str:
    sym = symbol(equation)
    print(sym)
    if sym == "add":
        return add(equation)
    if sym == "minus":
        return minus(equation)


if __name__ == "__main__":
    print(do_math("24 - 10"))
    print(do_math("12 + 12"))
