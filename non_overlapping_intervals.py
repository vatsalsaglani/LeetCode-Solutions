"""
leetcode: https://leetcode.com/problems/non-overlapping-intervals/
"""

def eraseOverlappingIntervals(intervals):

    if not intervals: return 0

    # sort intervals list with interval at end
    intervals.sort(key = lambda x: x[1])
    previousEnd, count = float("-inf"), 0

    for start, end in intervals:

        if start >= previousEnd:
            # no overlap
            previousEnd = end
        
        else:
            # overlap
            count += 1
    
    return count

    