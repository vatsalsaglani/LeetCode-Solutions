"""
leetcode: https://leetcode.com/problems/number-of-islands/
"""

import collections

def numIslands(grid):

    rows = len(grid)
    cols = len(grid[0])

    visited = set()
    islands = 0


    def bfs(r, c):

        q = collections.deque()
        visited.add((r, c))

        directions = [
            [1, 0], [-1, 0], [0, 1], [0, -1]
        ]

        while q:

            row, col = q.popleft()

            for dr, dc in directions:
                r, c = dr + row, dc + col

                if (
                    r in range(rows)
                    and 
                    c in range(cols)
                    and 
                    grid[r][c] == "1"
                    and 
                    (r, c) not in visited
                ):
                    visited.add((r, c))
                    q.append((r, c))
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and not (r, c) in visited:
                bfs(r, c)
                islands += 1
    
    return islands