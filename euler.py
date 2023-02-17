import math
import numpy as np
import matplotlib.pyplot as plt

def f(x, t):
    return (2 * math.exp(t**2 / 2))

def dx(x, t):
    return (x * t)

def euler(ti, tf, n):

    dt = (tf - ti) / (n - 1)
    x0 = f(0, ti)
    arr_x1 = []
    arr_x2 = []
    arr_t1 = np.linspace(ti, tf, int(n))
    arr_t2 = np.linspace(ti, tf, 1000)

    for i in range(1000):
        arr_x2.append(f(x0, arr_t2[i]))

    for i in range(int(n)):
        x1 = x0 + dt * dx(x0, dt * i)
        x0 = x1
        arr_x1.append(x1)
    
    plt.plot(arr_t1, arr_x1, c='r', label='euler')
    plt.plot(arr_t2, arr_x2, c='g', label='function')
    plt.title('Euler Method - 10 Points')
    plt.xlabel('t')
    plt.ylabel('x')
    plt.legend()
    plt.show()

def main():
    euler(0, 2, 10.0)

main()