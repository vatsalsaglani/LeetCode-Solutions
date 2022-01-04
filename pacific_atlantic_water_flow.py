"""
leetcode: https://leetcode.com/problems/pacific-atlantic-water-flow/
"""

def pacificAtlantic(heights):

    M, N = len(heights), len(heights[0])

    # coordinates for pacific and atlantic
    pacific, atlantic = [], []

    ## sets to stroe coordinates where water from pacific and atlantic flows respectively
    visited_pacific, visited_atlantic = set(), set()

    # initialize pacific coordinates and atlantic coordinates
    for r in range(M):
        # on the left start
        pacific.append((r, 0))
        # on the right end
        atlantic.append((r, N-1))
    

    
    for c in range(N):
        # taking 0 line at top
        pacific.append((0, c))
        # at the end
        atlantic.append((M - 1, c))

    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def dfs(r, c, visited):

        visited.add((r, c))
        for dr, dc in directions:
            row, col = dr + r, dc + c

            if (
                row in range(M)
                and 
                col in range(N)
                and 
                heights[r][c] <= heights[row][col]
                and
                not
                (row, col) in visited
            ):
                dfs(row, col, visited)
    

    for row, col in pacific: dfs(r, c, visited_pacific)
    for row, col, in atlantic: dfs(row, col, visited_atlantic)

    return visited_pacific & visited_atlantic
