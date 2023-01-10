# Array, Sorting
# Google 6 Amazon 2 Bloomberg 2 Microsoft 8 Facebook 5 Adobe 2 Apple 2 Wayfair 2
# https://leetcode.com/problems/meeting-rooms/description/
# Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.

# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false

# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: true


from typing import List

# brute force: compare every pair time O(m*n)
class MeetingRooms:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals_count = len(intervals)
        for i in range(0, intervals_count):
            for j in range(i + 1, intervals_count):
                if self.has_overlap(intervals[i], intervals[j]):
                    return False

        return True

    def has_overlap(self, interval1: List[int], interval2: List[int]) -> bool:
        start1 = interval1[0]
        end1 = interval1[1]
        start2 = interval2[0]
        end2 = interval2[1]
        no_overlap = end2 <= start1 or end1 <= start2

        return not no_overlap


# sort then compare time O(nlogn)
class MeetingRooms2:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals_copy = list()
        for interval in intervals:
            intervals_copy.append(Interval(interval[0], interval[1]))

        sorted_intervals = sorted(intervals_copy)
        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i - 1].end > sorted_intervals[i].start:
                return False

        return True


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        if self.start == other.start:
            return self.end < other.end

        return self.start < other.start
