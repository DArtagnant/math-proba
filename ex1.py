from refresh_plot import subplots, refresh_show, add_bars, add_text
from pieces import urne_jetons as de_pile

REFRESH_SPEED = 50
pile_count = 0
face_count = 0

def main(refresh):
    global pile_count, face_count
    if de_pile():
        pile_count += 1
    else:
        face_count += 1
    if (pile_count + face_count) % REFRESH_SPEED == 0:
        fig, ax = refresh()
        add_bars(ax,
                 (pile_count, face_count),
                 (f"{pile_count}", f"{face_count}")
                 )
        add_text(ax, f"{pile_count}, {face_count}")

if __name__ == "__main__":
    fig, ax = subplots()
    refresh_show(fig, ax, main)