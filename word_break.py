"""
leetcode: https://leetcode.com/problems/word-break/
"""

def wordBreak(s, wordDict):

    def bfs(s):

        memory = set()

        q = [s]

        while q:

            rem = q.pop(0)

            if not rem:
                return True

            if not rem in memory:
                memory.add(rem)
                for word in wordDict:
                    l = len(word)
                    if rem[:l] == word:
                        q.append(rem[l:])
    
        return False
    
    return bfs(s)