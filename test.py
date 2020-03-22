from main import add, minus, symbol, do_math

def test_add():
    x = "12 + 5"
    assert type(add(x)) == str
    assert add(x) == "17"


def test_minus():
    x = "12 - 5"
    assert type(minus(x)) == str
    assert minus(x) == "7"


def test_symbol():
    x = "12 - 5"
    assert symbol(x) == "minus"


def test_do_math():
    x = "24 - 10"
    y = "12 + 10"
    assert type(do_math(x)) == str
    assert do_math(x) == "14"
    assert do_math(y) == "22"