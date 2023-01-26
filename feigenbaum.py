def feigenbaum():
	d = 5
	m0 = 2
	m1 = 1 + 5 ** (1/2)
	
	for i in range(2, 10):
		n = 2 ** i
		u = m1 + (m1 - m0) / d
		for j in range(5):
			x0 = 1/2
			dx0 = 0
			for k in range(n):
				x1 = u * x0 * (1 - x0)
				dx1 = x0 * (1 - x0) + u * dx0 * (1 - 2 * x0)
				x0 = x1
				dx0 = dx1
			u = u - (x0 - 1/2) / dx0
		d = (m1 - m0) / (u - m1)
		m0 = m1
		m1 = u
	return (d)
	
def main():
	print(feigenbaum())

main()