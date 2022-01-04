"""
https://leetcode.com/problems/word-search/
"""


def exist(board, word):

    path = set()

    ROWS, COLS = len(board), len(board[0])

    def dfs(row, col, ix):

        if ix == len(word):
            return True

        if (row < 0 or col < 0 or row >= ROWS or col >= COLS
                or word[ix] != board[row][col] or (row, col) in path):
            return False

        path.add((row, col))

        res = (dfs(row + 1, col, ix + 1) or dfs(row - 1, col, ix + 1)
               or dfs(row, col - 1, ix + 1) or dfs(row, col + 1, ix + 1))

        path.remove((row, col))

        return res

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0): return True

    return False
