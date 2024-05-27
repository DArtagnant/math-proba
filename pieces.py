from random import randint

#ex 16 1
def lance_equilibre():
    return bool(randint(0, 1))

#ex 16 2
def lance_truque():
    return randint(1, 5) <= 3

#ex 17
def urne_jetons():
    return randint(1, 12) <= 5