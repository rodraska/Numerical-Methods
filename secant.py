def f(x):
	return (x ** 2 - 2)

def secant(nmax, tol):
	x0 = 5
	x1 = 2
	n = 0
	while (n <= nmax):
		x2 = x1 - f(x1) * (x1 - x0) / float(f(x1) - f(x0))
		if f(x2) == 0 or abs(x2 - x1) < tol:
			break
		else:
			x0 = x1
			x1 = x2
		n += 1
	if n < nmax:
		return (x2)
	else:
		return ("Method Failed")

def main():
	print(secant(5, 0.001))

main()
