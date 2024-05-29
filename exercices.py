from random import randint
from ex_type import *


def ex16_1():
    ex_type_2_bars("Pile", "Face", lambda: bool(randint(0, 1)))

def ex16_2():
    ex_type_2_bars("Pile", "Face", lambda: randint(1, 5) <= 3)

def ex17():
    ex_type_2_bars("Noir", "Blanc", lambda: randint(1, 12) <= 5)

def ex18():
    ex_type_2_bars("Blanc", "Noir", lambda: randint(1, 5) <= 3)

def partie_ex20():
    points = 0
    for _ in range(5):
        points += randint(0, 6)
        if points >= 20:
            return True
    return False

def ex20_bonus():
    ex_type_2_bars("gagné", "perdu", partie_ex20)

def ex20():
    gain = 0
    tour = 0
    while True:
        tour += 1
        if partie_ex20():
            gain += 5
        else:
            gain -= 5
        if tour % 200000 == 0:
            print(f"Gains : {gain}, Moyenne par tour : {gain / tour}")

def partie_ex21():
    for _ in range(6):
        if randint(0, 6) == 6:
            return True
    return False

def ex21():
    ex_type_2_bars("Lièvre", "Tortue", partie_ex21)

if __name__ == "__main__":
    ex21()