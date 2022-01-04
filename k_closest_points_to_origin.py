import heapq

def kClosest(points, k):

    def eucDist(point):

        x1, y1 = 0, 0
        x2, y2 = point

        return ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    
    dist = [(eucDist(p), p) for p in points]

    heapq.heapify(dist)

    op = []

    for i in range(k):

        itm = heapq.heappop(dist)
        op.append(itm[1])
    
    return op