# Array, Two Pointers
# Facebook 2 Uber 2 Yandex 2 Microsoft 3 Google 2 Bloomberg 2 Amazon 7 Apple 6 Oracle 2 Paypal 2 DoorDash
# https://leetcode.com/problems/interval-list-intersections/

# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi]
# and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that are either empty or represented
# as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

# Example 1:
# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

# Example 2:
# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []

from typing import List

# use two pointers to track both lists and merge intervals
# check overlap and move pointer with smaller end
# no overlap: max(start) > min(end)
# [ ]               [ ]
#    [ ]         [ ]
# has overlap: max(start) <= min(end)   => intersection =[max_start, min_end]
# [ ]              [ ]
#  [ ]            [ ]
class IntervalListIntersections:
    def intervalIntersection(
        self, list1: List[List[int]], list2: List[List[int]]
    ) -> List[List[int]]:
        intersections = list()

        list1_pointer = 0
        list2_pointer = 0
        while list1_pointer < len(list1) and list2_pointer < len(list2):
            interval1 = list1[list1_pointer]
            interval2 = list2[list2_pointer]
            max_start = max(interval1[0], interval2[0])
            min_end = min(interval1[1], interval2[1])
            if max_start <= min_end:
                intersections.append([max_start, min_end])

            # move pointer for smaller end interval
            if interval1[1] < interval2[1]:
                list1_pointer += 1
            else:
                list2_pointer += 1

        return intersections
