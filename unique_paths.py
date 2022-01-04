"""
leetcode: https://leetcode.com/problems/unique-paths/
"""

# same to grid traveller

def uniquePaths(m, n):

    def travel(m, n, memory = {}):

        if (m, n) in memory: return memory[m, n]
        if (n, m) in memory: return memory[n, m]

        if m == 1 and n == 1: return 1
        if m == 0 or n == 1: return 0

        memory[m, n] = travel(m-1, n, memory) + travel(m, n-1, memory)

        return memory[m, n]
    
    return travel(m, n)