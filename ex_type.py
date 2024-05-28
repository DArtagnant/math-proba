from refresh_plot import subplots, Refresher, UpdatableBar

REFRESH_TOUR = 20

def ex_type_2_bars(name1, name2, evenement):
    r = Refresher(*subplots())
    b1, b2 = UpdatableBar.create_bars(r, name1, name2)
    r.init_elem()
    tour = 0
    while True:
        if evenement():
            b1.value += 1
        else:
            b2.value += 1
        
        if tour % REFRESH_TOUR == 0:
            r.update()
        tour += 1