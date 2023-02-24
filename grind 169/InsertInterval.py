# Array
# Google 5 Amazon 3 Apple 3 LinkedIn 8 Facebook 7 Robinhood 4 Microsoft 3 Uber 2 Bloomberg 2 ByteDance 2 Walmart Global Tech 2
# Twitter 7 Zillow 3 Reddit 3 Dataminr 2 Goldman Sachs 2 Salesforce 2 Citadel 2
# https://leetcode.com/problems/insert-interval/

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
# represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and
# intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


# find the newInterval position in intervals (either by binary search or linear search)
# insert newInterval to intervals
# iterate through new intervals and merge if needed
# time search logn + insert n + merge n = n
# space merged n, space optimize can be done via reversed intervals, merge two by two, and reverse back
class InsertInterval:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        insert_position = bisect.bisect(intervals, newInterval)  # logn
        intervals.insert(insert_position, newInterval)  # n

        merged_intervals = list()
        for interval in intervals:
            if self.has_overlap(merged_intervals, interval):
                new_end = max(merged_intervals[-1][1], interval[1])
                merged_intervals[-1][1] = new_end
            else:
                merged_intervals.append(interval)

        return merged_intervals

    def has_overlap(self, merged_intervals: List[List[int]], next_interval: List[int]):
        if not merged_intervals:
            return False

        _, last_merged_end = merged_intervals[-1]
        next_start, _ = next_interval

        return last_merged_end >= next_start
