def f(x):
    return (x ** 3 + 3 * x ** 2 + 4 * x - 10)

def bisection(nmax, tol):
    n = 0
    x0 = -10
    x1 = 10
    while n <= nmax:
        x2 = (x0 + x1) / 2
        if f(x2) == 0 or (x1 - x0) / 2 < tol:
            return (x2)
        else:
            if f(x0) * f(x2) < 0:
                x1 = x2
            elif f(x0) * f(x1) < 0:
                x0 = x2
        n += 1
    if n < nmax:
        return (x2)
    else:
        return ("Method Failed")

def main():
    print(bisection(100, 0.01))

main()      