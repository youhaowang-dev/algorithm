# Array, Sorting
# Amazon 27 Bloomberg 24 Facebook 19 Google 9 Microsoft 8 Adobe 8 Uber 8 Apple 6 Yahoo 4 Cisco 3
# Palantir Technologies 3 Salesforce 3 Yandex 3 Paypal 2 eBay 2 Oracle 2 Coupang 2 Booking.com 2 Expedia 2
# ByteDance 2 TikTok 2 Cognizant 2 IBM 7 LinkedIn 6 Walmart Global Tech 6 VMware 6 Shopee 6 Snapchat 4 Nvidia 4
# Morgan Stanley 3 Goldman Sachs 2 Twitter 2 Pinterest 2 Atlassian 2 Qualtrics 2 Hotstar JPMorgan 70 Splunk 7
# Reddit 5 Wish 4 Intuit 3 DoorDash 3 Zillow 3 Visa 3 Twilio 3 Tesla 3 Nutanix 2 Netflix 2 ServiceNow 2 Two Sigma 2
# BlackRock 2 Houzz 2 Robinhood 2 Tableau 2 Citadel 2 Arcesium 2 Yelp Wix
# https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

from typing import List


class MergeIntervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        get_sort_key = lambda interval: interval[0]
        sorted_intervals = sorted(intervals, key=get_sort_key)

        merged = list()
        for interval in sorted_intervals:
            if self.has_overlap(merged, interval):
                # merge by updating end
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)

        return merged

    # last_merged exists and last_merged.end > next.start
    def has_overlap(self, merged: List[List[int]], interval: List[int]):
        return merged and merged[-1][1] >= interval[0]
