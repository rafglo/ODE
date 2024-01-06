import pandas as pd
from itertools import count
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


def populacje(Z_0, W_0, a, b, r, s, n, h):
    wilki = [W_0]
    zajace = [Z_0]
    for i in range(n):
        W = float(wilki[-1])
        Z = float(zajace[-1])
        zajace.append(Z+(r*Z - a*Z*W)*h)
        wilki.append(W+(-s*W + b*a*Z*W)*h)

    return zajace, wilki

import matplotlib.pyplot as plt
a = 0.002
b = 1.25
r = 0.1
s = 0.2
n = 1000
h = 0.2
ts = [i for i in range(0, n+1)]
zajace, wilki = populacje(80, 20, a, b, r, s, n, h)


fig, ax = plt.subplots()
ax.axis([0, n, 0, 200])
line2 = ax.plot(ts[0], zajace[0])[0]
line1 = ax.plot(ts[0], wilki[0])[0]

def update(frame):
    line2.set_xdata(ts[:frame])
    line2.set_ydata(zajace[:frame])
    line1.set_xdata(ts[:frame])
    line1.set_ydata(wilki[:frame])


ani = animation.FuncAnimation(fig=fig, func=update, frames=1000, interval=30)
plt.show()

"""fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    xs = []
    ys = []
    for i in range(n):
        xs.append(ts[i])
        ys.append(zajace[i])
    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()"""


