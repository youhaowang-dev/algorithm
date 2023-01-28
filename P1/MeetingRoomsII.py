# Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum
# Bloomberg 42 Amazon 25 Google 15 Facebook 5 Apple 4 Walmart Global Tech 4 Uber 2 Microsoft 18 Oracle 9 eBay 4 ByteDance 3 Paypal 2 Visa 2 Goldman Sachs 2 TikTok 2 Adobe 6 Yandex 6 Twitter 4 Snapchat 4 Qualtrics 4 VMware 3 Quora 3 Swiggy 3 Intuit 2 Yahoo 2 Expedia 2 GoDaddy 2 Salesforce 2 Splunk 2 Redfin 2 Docusign 2
# https://leetcode.com/problems/meeting-rooms-ii/
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: 1

from heapq import heappop, heappush
from typing import List

class MeetingRoomsII1:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        max_count = 0
        count = 0
        time_count_deltas = list()
        for start, end in intervals:
            time_count_deltas.append((start, 1))
            time_count_deltas.append((end, -1))
        
        time_count_deltas.sort()
        for _, count_delta in time_count_deltas:
            count += count_delta
            max_count = max(max_count, count)

        return max_count

class MeetingRoomsII2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        get_sort_key = lambda x: x[0]
        intervals.sort(key=get_sort_key)

        end_times_min_heap = []
        heappush(end_times_min_heap, intervals[0][1])

        for interval in intervals[1:]:

            min_end_time = end_times_min_heap[0]  # [0] is python min heap peek
            if min_end_time <= interval[0]:
                # no need to have new room
                heappop(end_times_min_heap)

            # need new room
            heappush(end_times_min_heap, interval[1])

        return len(end_times_min_heap)


# https://leetcode.com/problems/meeting-rooms-ii/solutions/423462/
# brute force: We are going to simulate real case.
# We just have to find room where meeting is already finished
# If we cannot find such room - just add a new one
# time O()
class MeetingRoomsII3:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        meetings: List[List[int]] = list()
        for meeting in intervals:
            self.start_meeting(meetings, meeting)

        return len(meetings)

    def start_meeting(self, meetings: List[List[int]], meeting: List[int]) -> None:
        for i in range(0, len(meetings)):
            if meetings[i][1] <= meeting[0]:
                meetings[i] = meeting
                return

        meetings.append(meeting)
