from matplotlib import pyplot as plt

text_place = None

def subplots():
    return plt.subplots()

def add_bars(ax, bars, labels):
    for n, (bar, label) in enumerate(zip(bars, labels)):
        mbar = ax.bar(n, bar)
        ax.bar_label(mbar, label_type='center')

def add_text(ax, text_label):
    text_place.set_text(text_label)

def refresh_show(fig, ax, callback):
    global text_place
    text_place = ax.text(0.5, 0.02, "")
    wait_wanted = False
    def refresh_inner():
        nonlocal wait_wanted
        ax.clear()
        ax.set_xticklabels([])
        wait_wanted = True
        return fig, ax
    while True:
        callback(refresh_inner)
        if wait_wanted:
            wait_wanted = False
            plt.pause(0.00005)