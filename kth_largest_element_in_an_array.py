import heapq

def findKthLargest(nums, k):

    a = [-i for i in nums]
    heapq.heapify(a)
    n = 0
    for i in range(k):
        n += 1
        itm = heapq.heappop(a)
        if n == k:
            return -1 * itm