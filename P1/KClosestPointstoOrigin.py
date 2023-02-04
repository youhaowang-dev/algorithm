# Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect
# https://leetcode.com/problems/k-closest-points-to-origin

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# O(nlogk + k)
class KClosestPointstoOrigin:
    def kClosest(self, points: List[List[int]], needed: int) -> List[List[int]]:
        if not points:
            return list()

        min_heap = list()

        for x, y in points:
            distance = -(x*x + y*y)
            heapq.heappush(min_heap, (distance, x, y))
            if len(min_heap) > needed:
                heapq.heappop(min_heap)

        return [[x, y] for (_, x, y) in min_heap]
