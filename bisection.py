def f(x):
    return (x ** 2 - 2)

def bisection(nmax, tol):
    n = 0
    x0 = 0
    x1 = 10
    while n <= nmax:
        x2 = (x0 + x1) / 2
        if f(x2) == 0 or (x1 - x0) / 2 < tol:
            break
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
    print(bisection(30, 0.0000001))

main() 