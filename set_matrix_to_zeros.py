"""
Leetcode: https://leetcode.com/problems/set-matrix-zeroes/submissions/
"""

def setZeros(matrix):

    ## make two row and col arrays to keep track of which 
    # row and column needs to be converted to zero

    M, N = len(matrix), len(matrix[0])
    row, col = [1]*M, [1]*N

    # mark row and col to make zero
    for r in range(M):
        for c in range(N):
            if matrix[r][c] == 0:
                row[r] = 0
                col[c] = 0

    # update rows
    for r in range(M):
        if row[r] == 0:
            matrix[r] = [0]*N
    
    # update columns
    for c in range(N):
        if col[c] == 0:
            for i in range(M):
                matrix[i][c] = 0
    
    return matrix

# with constant space

def setZeros(matrix):

    # use first row and column to keep of track of where 
    # we need to put zeros instead of initializing two list

    M, N = len(matrix), len(matrix[0])

    firstrow, firstcol = False, False

    for r in range(M):
        if matrix[r][0] == 0:
            firstcol = True
    
    for c in range(N):
        if matrix[0][c] == 0:
            firstrow = True
    
    # tarverse from 1, we won't touch first col

    #  -------------------
    # |  X |    |    |    |
    # | ---| ---| ---| ---|
    # |  X |    |    |    |
    # | ---| ---| ---| ---|
    # |  X |    |    |    |
    #  -------------------

    # put zero in first row (inner row) when we get zero in matrix[r][c]
    #  -------------------
    # |  X |  I |  I |  I |
    # | ---| ---| ---| ---|
    # |  X |  I |    |    |
    # | ---| ---| ---| ---|
    # |  X |  I |    |    |
    #  -------------------
    for r in range(M):
        for c in range(1, N):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
    #  -------------------
    # |  X |  I |    |    |
    # | ---| ---| ---| ---|
    # |  X |  I |    |    |
    # | ---| ---| ---| ---|
    # |  X |  I |    |    |
    #  -------------------
    # put zero in first column (inner column) when we get zero in matrix[r][c]
    for r in range(1, M):
        for c in range(1, N):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
    
    # update rows

    for r in range(1, M):
        if matrix[r][0] == 0:
            matrix[r] = [0]*N
    

    # update columns

    for c in range(1, N):
        if matrix[0][c] == 0:
            for i in range(1, M):
                matrix[i][c] = 0
    
    if firstrow:
        matrix[0] = [0]*N
    
    if firstcol:
        for i in range(M):
            matrix[i][0] = 0
    
    return matrix
