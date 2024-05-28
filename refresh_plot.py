from matplotlib import pyplot as plt

WAIT_TIME = 0.01

def subplots():
    return plt.subplots()

class Refresher:
    def __init__(self, fig, ax):
        self.fig = fig
        self.ax = ax
        self._listener = []

    def add_listener(self, listener):
        self._listener.append(listener)
        return listener
    
    def init_elem(self):
        for l in self._listener:
            l.init_elem(self.fig, self.ax)
        plt.ion()
        plt.show()
        plt.pause(WAIT_TIME)
    
    def update(self):
        if any((l.need_update() for l in self._listener)):
            for l in self._listener:
                l.update(self.fig, self.ax)
            self.fig.canvas.draw()
            self.fig.canvas.flush_events()


class UpdatableBar:
    def __init__(self, name):
        self._name = name
        self._value = 0
        self._need_refresh = False

    @staticmethod
    def create_bars(refresher, *names):
        return (refresher.add_listener(UpdatableBar(name)) for name in names)

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._need_refresh = True
        self._value = value
    
    def init_elem(self, fig, ax):
        self.bar = ax.bar(self._name, self._value)[0]
    
    def need_update(self):
        return self._need_refresh
    
    def update(self, fig, ax):
        self.bar.set_height(self._value)
        ax.set_ylim(0, max(self._value * 1.1, ax.get_ylim()[1]))
        self._need_refresh = False