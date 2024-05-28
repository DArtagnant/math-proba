from random import randint
from ex_type import *


def ex1():
    ex_type_2_bars("A", "B", lambda: bool(randint(0, 1)))

#ex 16 1
def lance_equilibre():
    return bool(randint(0, 1))

#ex 16 2
def lance_truque():
    return randint(1, 5) <= 3

#ex 17
def urne_jetons():
    return randint(1, 12) <= 5

if __name__ == "__main__":
    ex1()