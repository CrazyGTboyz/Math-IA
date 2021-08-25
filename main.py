from itertools import count
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn')

x_vals = []
y_vals = []

index = count()

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
print(ax1)
print(ax2)

def animate(i):
    data = pd.read_csv('w_drag_data.csv')
    x = data['x_pos']
    y = data['y_pos']

    ax1.cla()
    ax1.plot(x, y, label='Position')

    ax1.legend(loc='upper left')
    plt.tight_layout()

def animate2(i):
    data = pd.read_csv('wo_drag_data.csv')
    x = data['x_pos']
    y = data['y_pos']

    ax2.cla()
    ax2.plot(x, y, label='Position')

    ax2.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

ani2 = FuncAnimation(plt.gcf(), animate2, interval=1000)

plt.tight_layout()
plt.show()