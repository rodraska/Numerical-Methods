import math
import numpy as np
import matplotlib.pyplot as plt

def f(x, t):
    return (2 * math.exp(t**2 / 2))

def dx(x, t):
    return (x * t)

def rk2(ti, tf, n):

    dt = (tf - ti) / (n - 1)
    x0 = f(0, ti)
    arr_x1 = []
    arr_x2 = []
    arr_t1 = np.linspace(ti, tf, int(n))
    arr_t2 = np.linspace(ti, tf, 1000)

    for i in range(1000):
        arr_x2.append(f(x0, arr_t2[i]))
    
    for i in range(int(n)):
        k1 = dt * dx(x0, dt * i)
        k2 = dt * dx(x0 + k1 / 2, dt * i + dt / 2)
        x1 = x0 + k2
        arr_x1.append(x0)
        x0 = x1

    plt.plot(arr_t1, arr_x1, c='r', label='RK2')
    plt.plot(arr_t2, arr_x2, c='g', label='function')   
    plt.title('RK2 Method - 10 Points')
    plt.xlabel('t')
    plt.ylabel('x')
    plt.legend()
    plt.show()

def main():
    rk2(0, 2, 10)

main()