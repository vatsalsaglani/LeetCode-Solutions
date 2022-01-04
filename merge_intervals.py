"""
leetcode: https://leetcode.com/problems/merge-intervals/
"""

def mergeIntervals(intervals):

    # sort by start in interval
    intervals.sort(key = lambda x: x[0])

    output = [intervals[0]]

    for start, end in intervals[1:]:
        lastEnd = output[-1][1]
        if start <= lastEnd:
            # overlap
            output[-1][1] = max(output[-1][1], end)
        else:
            # no overlap append to output
            output.append([start, end])
    
    return output