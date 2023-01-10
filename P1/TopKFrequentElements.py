# Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect
# Amazon 24 Facebook 11 Google 5 Microsoft 4 Apple 4 Bloomberg 3 Uber 3 Adobe 2 ByteDance 2 Tesla 2 Oracle 5 Snapchat 3 Indeed 3 Cisco 3 Netflix 3 Shopee 3 Twitter 2 Yahoo 2 eBay 2 VMware 2 TikTok 2 Arcesium 2 Deloitte 2 Yelp 6 Walmart Global Tech 6 Capital One 5 Salesforce 3 HBO 3 LinkedIn 2 Dropbox 2 Expedia 2 Twilio 2 Paypal 2 Wish 2 C3 IoT 2 Zynga 2 Cashfree 2 Pocket Gems
# https://leetcode.com/problems/top-k-frequent-elements/description/

# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


from heapq import heappop, heappush
from typing import Dict, List, Tuple


# brute force: dict to count frequency, then sort dict.items(), then build and return result
class TopKFrequentElements:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = dict()
        for num in nums:
            num_to_count[num] = 1 + num_to_count.get(num, 0)

        num_to_count_entries = num_to_count.items()
        get_sort_key = lambda entry: -entry[1]
        sorted_num_to_count_entries = sorted(num_to_count_entries, key=get_sort_key)

        result = list()
        for i in range(0, k):
            result.append(sorted_num_to_count_entries[i][0])

        return result


# quick select O(n)
# partition the array to make frequency on target_index left < frequency on target_index right
class TopKFrequentElements2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = dict()
        for num in nums:
            num_to_count[num] = 1 + num_to_count.get(num, 0)

        unique_nums = list(num_to_count.keys())
        unique_count = len(num_to_count)

        start = 0
        end = unique_count - 1
        target_index = unique_count - k
        self.quickselect(
            unique_nums, num_to_count, 0, unique_count - 1, unique_count - k
        )

        return unique_nums[unique_count - k : unique_count]

    def quickselect(
        self,
        nums: List[int],
        num_to_count: Dict[int, int],
        start: int,
        end: int,
        target_index: int,
    ) -> None:
        if start == end:
            return

        pivot = (end + start) // 2

        sorted_pivot = self.partition(nums, num_to_count, start, end, pivot)

        if target_index == sorted_pivot:
            # frequency on target_index left < frequency on target_index right
            return
        elif target_index < sorted_pivot:
            self.quickselect(nums, num_to_count, start, sorted_pivot - 1, target_index)
        else:
            self.quickselect(nums, num_to_count, sorted_pivot + 1, end, target_index)

    def partition(
        self,
        nums: List[int],
        num_to_count: Dict[int, int],
        start: int,
        end: int,
        pivot: int,
    ) -> None:
        pivot_count = num_to_count.get(nums[pivot])
        # 1. move pivot to end
        self.swap(pivot, end, nums)
        sorted_pivot = start

        # 2. move all less frequent elements to the start
        for i in range(start, end + 1):
            if num_to_count.get(nums[i]) < pivot_count:
                self.swap(sorted_pivot, i, nums)
                sorted_pivot += 1

        # 3. move pivot to its final place
        self.swap(sorted_pivot, end, nums)

        return sorted_pivot

    def swap(self, a: int, b: int, nums: List[int]) -> None:
        (nums[a], nums[b]) = (nums[b], nums[a])


# maintain a min heap with size k and transfer all values to result
# time O(nlogk)
class TopKFrequentElements3:

    # build count
    # build heap
    # build result
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = dict()
        for num in nums:
            num_to_count[num] = num_to_count.get(num, 0) + 1

        min_heap = []
        for item in num_to_count.items():
            heappush(min_heap, NumFrequencyPair(item))
            if len(min_heap) > k:
                heappop(min_heap)

        result = []
        while min_heap:
            result.append(heappop(min_heap)[0])

        return result


# Tuple[int, int] [0] is num [1] is frequency
class NumFrequencyPair(Tuple[int, int]):
    def __init__(self, pair: Tuple[int, int]):
        self.pair = pair

    # custom comparator
    def __lt__(self, other):
        return self[1] < other[1]
