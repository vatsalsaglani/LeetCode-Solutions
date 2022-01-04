"""
https://leetcode.com/problems/top-k-frequent-elements/
"""

import collections

def topKFrequent(numbers, k):

    c = collections.Counter(numbers)
    c = [(v, k) for k, v in c.items()]
    c.sort(key = lambda i: i[0], reverse = True)
    output = []
    for i in range(k):
        output.append(c[i][1])
    
    return output

import heapq

def topKFrequent(numbers, k):

    c = collections.Counter(numbers)
    c = [(-v, k) for k, v in c.items()]
    # max heap
    heapq.heapify(c)
    output = []
    for i in range(k):
        item = heapq.heappop(c)
        output.append(item[1])
    
    return output