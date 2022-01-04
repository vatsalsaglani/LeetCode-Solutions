"""
https://leetcode.com/problems/coin-change/
"""

def coinChange(coins, amount):
    return bestSum(amount, coins)

def bestSum(target, numbers):

    if target == 0: return 0

    table = [None] * (target + 1)

    table[0] = []

    for ix in range(target + 1):
        if table[ix] is not None:
            for number in numbers:
                if ix + number < target + 1:
                    combination = [*table[ix], number]

                    if not table[ix+number] or len(table[ix+number]) > len(combination):
                        table[ix+number] = combination
    
    if table[target]:
        return len(table[target])
    else:
        return -1