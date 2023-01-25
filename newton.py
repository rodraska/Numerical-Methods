def f(x):
	return (x ** 2 - 2)

def df(x):
	return (2 * x)

def newton(x0, nmax, tol):
	n = 0
	while (n <= nmax):
		x1 = x0 - f(x0) / df(x0)
		if f(x1) == 0 or abs(x1 - x0) < tol:
			break
		else:
			x0 = x1
		n += 1
	if n < nmax:
		return (x1)
	else:
		return ("Method Failed")

def main():
	print(newton(1.5, 5, 0.0001))

main()


