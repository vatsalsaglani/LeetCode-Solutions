"""
leetcode: https://leetcode.com/problems/longest-common-subsequence/
"""


def longestCommonSubSequence(text1, text2):

    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]  # 1 + value in diagonal
            else:
                dp[i][j] = max(dp[i][j + 1],
                               dp[i + 1][j])  # max of right, bottom

    return dp[0][0]
