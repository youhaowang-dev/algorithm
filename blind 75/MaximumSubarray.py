# Array, Divide and Conquer, Dynamic Programming
# Amazon 41 Apple 10 Microsoft 9 Adobe 9 Google 8 Cisco 8 Facebook 6 LinkedIn 5 Bloomberg 5 Expedia 3 Uber 3 JPMorgan 3 Twilio 3 Oracle 2 DE Shaw
# https://leetcode.com/problems/maximum-subarray/
# Given an integer array nums, find the subarray which has the largest sum and return its sum.
# example: maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) => 6 because [4,-1,2,1] has the largest sum = 6

# time n space n
# maintain a prefix sum and a min prefix sum, max sub arr sum = max(prefix sum - min prefix sum)
class MaximumSubarray0:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_subarr_sum = nums[0]  # important for negative number
        prefix_sum = 0
        min_prefix_sum = 0
        for num in nums:
            prefix_sum += num
            max_subarr_sum = max(max_subarr_sum, prefix_sum - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum)

        return max_subarr_sum


# time n space n
# build the prefix_sum and track the minPrefix_sum(0 or lower)
# maxSum=max(maxSum, currentPrefix_sum - minPrefix_sum)
class MaximumSubarray:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -(2**31)
        min_prefix_sum = 0

        prefix_sum = self.get_prefix_sum(nums)
        # dont need the 0
        for i in range(1, len(prefix_sum)):
            max_sum = max(max_sum, prefix_sum[i] - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum[i])

        return max_sum

    # sum(i) = sigma(0 to i)
    # [1,2,3] => [0,1,3,6]
    def get_prefix_sum(self, nums: List[int]) -> int:
        prefix_sum = list()
        prefix_sum.append(0)

        for i in range(1, len(nums) + 1):
            prefix_sum.append(prefix_sum[i - 1] + nums[i - 1])

        return prefix_sum


# brute force: find all subarrays and get the sums
# time complexity: O(n^2) all subarrays * O(n) subarray sum = O(n^3)
# space complexity: O(1) for no extra space usage
class MaximumSubarray2:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray_sum = -(2**31)

        if not nums:
            return max_subarray_sum

        for left in range(0, len(nums)):
            for right in range(left, len(nums)):
                subarray_sum = self.getSubArraySum(left, right, nums)
                max_subarray_sum = max(max_subarray_sum, subarray_sum)

        return max_subarray_sum

    def getSubArraySum(self, left, right, nums: List[int]):
        sum = 0
        for i in range(left, right + 1):
            sum += nums[i]

        return sum
