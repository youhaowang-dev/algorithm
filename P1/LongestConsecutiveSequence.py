# Array, Hash Table, Union Find
# Google 11 Amazon 10 Adobe 5 Apple 5 Bloomberg 4 Facebook 2 Microsoft 2 Spotify 4 Visa 2 Qualtrics 2 eBay 2 Morgan Stanley 2 LinkedIn 4 Zillow 3 Goldman Sachs 3 Salesforce 3 Uber 2 Cohesity 2 Twitter 2 Cisco 2
# https://leetcode.com/problems/longest-consecutive-sequence/description/

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
# Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9

# one pass O(n): make sure num is the start by checking num-1, then check num+1
class LongestConsecutiveSequence:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        max_length = 0
        for num in num_set:
            prev_num = num - 1
            if prev_num in num_set:
                continue  # we only care the start of a sequence, so O(n)

            length = 1
            next_num = num + 1
            while next_num in num_set:
                length += 1
                next_num += 1
            max_length = max(max_length, length)

        return max_length

# brute force O(n^3): get length for each num, maintain a max


class LongestConsecutiveSequence2:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0

        for num in nums:
            length = 1
            number = num
            while (self.hasNextConsecutive(nums, number + 1)):
                number += 1
                length += 1

            max_length = max(max_length, length)

        return max_length

    def hasNextConsecutive(self, nums: List[int], target: int) -> bool:
        for num in nums:
            if num == target:
                return True

        return False
