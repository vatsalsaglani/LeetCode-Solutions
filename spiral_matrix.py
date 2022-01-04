"""
Leetcode: https://leetcode.com/problems/spiral-matrix/
"""


def spiralMatrix(matrix):

    res = []
    left, right = 0, len(matrix[0])  # 0, columns
    top, bottom = 0, len(matrix)  # 0, rows

    while left < right and top < bottom:

        # get all values in top row
        for i in range(left, right):
            res.append(matrix[top][i])

        top += 1

        # get all values in right column
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])  # right is one off

        right -= 1

        # if it's 1 row or 1 col matrix

        if not (left < right and top < bottom):
            break

        # get value bottom row in reverse

        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])

        bottom -= 1

        # get values of left column in reverse bottom up

        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])

        left += 1

    return res