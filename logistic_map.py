import numpy as np
import matplotlib.pyplot as plt

def function(x, u, n):
    if n == 300:
        return (x)
    return (function(u * x * (1 - x), u, n + 1))

def logistic():
    fig, biax = plt.subplots()
    fig.set_size_inches(16, 9)
    interval_u = np.linspace(2.8, 4, 10000)
    interval_x = [0] * 200
    for u in interval_u:
        xf = function(0.5, u, 0)
        for i in range(200):
            xf = function(xf, u, 299)
            interval_x[i] = xf
        biax.plot([u] * 200, interval_x, 'b.', markersize = 0.01)
    biax.set(xlabel='u', ylabel='x', title='logistic map')
    plt.show()

def main():
    logistic()

main()