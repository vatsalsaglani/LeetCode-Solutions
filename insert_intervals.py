"""
leetcode: https://leetcode.com/problems/insert-interval/
"""


def insertInterval(intervals, newInterval):

    if not intervals:
        return [newInterval]

    output = []

    newStart, newEnd = newInterval

    N = len(intervals)

    i = 0

    # add original intervals till newStart
    while i < N and intervals[i][0] <= newStart:
        output.append(intervals[i])
        i += 1

    # insert newInterval or update the last interval in the output intervals list

    if not output:
        output.append(newInterval)
    elif output[-1][1] < newStart:
        # no overlap
        # append the newInterval directly
        output.append(newInterval)
    else:
        # overlap
        output[-1][1] = max(output[-1][1], newEnd)

    # add or update inteval for remaining intervals

    while i < N:
        newStart, newEnd = intervals[i]
        if output[-1][1] < newStart:
            # no overlap
            output.append([newStart, newEnd])
        else:
            # overlap
            output[-1][1] = max(output[-1][1], newEnd)
        i += 1

    return output