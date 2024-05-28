from refresh_plot import subplots, Refresher, UpdatableBar
from random import randint

REFRESH_TOUR = 2000
REFRESH_TEXT_TOUR = 200000

def ex_type_2_bars(name1, name2, evenement):
    r = Refresher(*subplots())
    b1, b2 = UpdatableBar.create_bars(r, name1, name2)
    r.init_elem()
    tour = 1
    while True:
        if evenement():
            b1.value += 1
        else:
            b2.value += 1
        
        if tour % REFRESH_TOUR == 0:
            r.update()
        if tour % REFRESH_TEXT_TOUR == 0:
            print(f"fréquence d'apparition de {name1} : {b1.value / tour} pour {tour} tours. En effet, il y a {b1.value} {name1}")
        tour += 1
