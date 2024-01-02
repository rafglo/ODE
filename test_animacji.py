import pandas as pd
from itertools import count
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

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

plt.style.use("ggplot")

def animate(i):
    plt.cla()
    x = ts 
    y = zajace 
    
    plt.plot(x,y)
    plt.xlabel("Czas")
    plt.ylabel("Wielkość populacji")
    plt.title("Symulacja modelu Lotki-Volterry")

ani = FuncAnimation(fig=plt.gcf(), func=animate, interval = 30, frames = 1, repeat = True)
plt.tight_layout()
plt.show()
