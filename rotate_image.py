"""
leetcode: https://leetcode.com/problems/spiral-matrix/
"""

def rotate(matrix):

    left, right = 0, len(matrix[0])-1

    while left < right:

        for i in range(right - left):

            top, bottom = left, right

            # save top left into a variable
            topLeft = matrix[top][left+i]

            # move bottom left to top left
            matrix[top][left+i] = matrix[bottom - i][left]

            # move bottom right to bottom left
            matrix[bottom-i][left] = matrix[bottom][right-1]

            # move top right to bottom right
            matrix[bottom][right - i] = matrix[top+i][right]

            # move topLeft saved to top right
            matrix[top+i][right] = topLeft

        # update left and right pointers
        right -= 1
        left += 1