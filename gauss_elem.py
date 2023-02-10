def gaussian(matrix):

    nr = len(matrix)
    nc = len(matrix[0])

    for r in range(0, nr - 1):
        
        for m in range(r + 1, nr):
            if (matrix[m][r] > matrix[r][r]):
                matrix[r], matrix[m] = matrix[m], matrix[r]
    
        for m in range(r + 1, nr):
            try:
                cof = -matrix[m][r] / matrix[r][r]
            except ZeroDivisionError:
                cof = 0
            for c in range(0, nc):
                matrix[m][c] += cof * matrix[r][c]
    
    for r in range(nr - 1, 0, -1):

        n = 0
        while (matrix[r][n] == 0):
            n += 1
        
        for m in range(r - 1, -1, -1):
            cof = -matrix[m][n] / matrix[r][n]
            for c in range(0, nc):
                matrix[m][c] += cof * matrix[r][c]

    for r in range(nr):
        
        n = 0
        while (matrix[r][n] == 0):
            n += 1

        x =  matrix[r][nc - 1] / matrix[r][n]
        print(f"x{r} = {x}")

def main():

    matrix = [[4, 7, 4, 0, 0],
              [1, 0, 4, 2, 1], 
              [0, 3, 0, 3, 2],
              [4, 0, 2, 0, 1]]
    
    gaussian(matrix)

main()