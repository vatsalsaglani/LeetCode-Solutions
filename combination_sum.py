"""
leetcode: https://leetcode.com/problems/combination-sum/
"""

# mug it
def combinationSum(candidates, target):

    dp = [[] for _ in range(len(target+1))]

    for c in candidates:
        for i in range(c, target+1):
            if i == c:
                dp[i].append([c])
            
            for comb in dp[i - c]:
                dp[i].append(comb + [c])
    
    return dp[-1]