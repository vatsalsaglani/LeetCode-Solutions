"""
leetcode: https://leetcode.com/problems/decode-ways/
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        memo = [-1 for i in range(len(s))]
        
        
        
        
        
        def helper(current, code, memo):
            if current == 0:
                if code[current] == '0':
                    memo[current] = 0
                    return 0
                else:
                    memo[current] = 1
                    return 1

            if current == -1: return 1

            if memo[current] != -1:
                return memo[current]

            # current at 0 but we can use previous element to form 10 or 20
            if code[current] == '0':
                if code[current - 1] == '1' or code[current - 1] == '2':
                    memo[current] = helper(current - 2, code, memo)
                    return memo[current]
                else:
                    memo[current] = 0
                    return memo[current]

            if code[current - 1] == '1' or code[current-1] == '2' and int(code[current]) < 7:
                ways = helper(current - 1, code, memo) + helper(current - 2, code, memo)

            else:
                ways = helper(current - 1, code, memo)

            memo[current] = ways
            return ways
        
        return helper(len(s)-1, s, memo)