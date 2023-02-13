import math

def xsq(x):
    return (x ** 2)

def cos(x):
    return (math.cos(x))

def midpoint(f, xi, xf):
    return ((xf - xi) * f((xf - xi) / 2))

def trapezoidal(f, xi, xf):
    return ((xf - xi) / 2 * (f(xi) + f(xf)))

def simpson(f, xi, xf):
    return ((xf - xi) / 6 * (f(xi) + 4 * f((xf - xi) / 2) + f(xf)))

def trap_comp(f, xi, xf, n):
    total = 0
    h = (xf - xi) / n
    x1 = xi
    x2 = xi + h
    for i in range(0, n):
        total += trapezoidal(xsq, x1, x2)
        x1 = x2
        x2 = x1 + h
    return (total)

def simp_comp(f, xi, xf, n):
    total = 0
    h = (xf - xi) / n
    x1 = xi
    x2 = xi + h
    for i in range(0, n):
        total += simpson(xsq, x1, x2)
        x1 = x2
        x2 = x1 + h
    return (total)

def main():
    print(midpoint(xsq, 0, math.pi))
    print(trapezoidal(xsq, 0, math.pi))
    print(simpson(xsq, 0, math.pi))
    print(trap_comp(xsq, 0, math.pi, 100))
    print(simp_comp(xsq, 0, math.pi, 100))

main()