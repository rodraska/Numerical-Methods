def subset(n):
	if n == 0:
		return ([[]])
	old_list = subset(n - 1)
	new_list = old_list[:]
	for old_elem in old_list:
		new_elem = old_elem[:]
		new_elem.append(n)
		new_list.append(new_elem)
	return (new_list)
	
def main():
	print(subset(3))

main()
