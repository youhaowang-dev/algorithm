# Array, Binary Search
# Coinbase 12 Salesforce 4 Airbnb 2 Expedia
# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor,
# divide all the array by it, and sum the division's result.
# Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

# Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

# The test cases are generated so that there will be an answer.

# Example 1:
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).
# Example 2:
# Input: nums = [44,22,33,11,1], threshold = 5
# Output: 44


from ast import List
from math import ceil

# linear search O(num_count * max_num)
class FindtheSmallestDivisorGivenaThreshold:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        min_divisor = 1
        max_divisor = max(nums)

        while min_divisor + 1 < max_divisor:
            if self.get_divide_result_sum(nums, min_divisor) > threshold:
                min_divisor += 1
                continue

            return min_divisor

        return max_divisor

    def get_divide_result_sum(self, nums: List[int], divisor: int):
        sum_of_division_results = 0
        for num in nums:
            sum_of_division_results += ceil(num / divisor)

        return sum_of_division_results


# binary search O(num_count * log(max_num))
class FindtheSmallestDivisorGivenaThreshold2:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        min_divisor = 1
        max_divisor = max(nums)

        while min_divisor + 1 < max_divisor:
            divisor = (min_divisor + max_divisor) // 2
            divide_result_sum = self.get_divide_result_sum(nums, divisor)
            if divide_result_sum > threshold:
                min_divisor = divisor
            if divide_result_sum < threshold:
                max_divisor = divisor
            if divide_result_sum == threshold:
                max_divisor = divisor
                # return divisor # cannot do this because integer divide round down; we can possibly use smaller divisor to get the same sum

        if self.get_divide_result_sum(nums, min_divisor) <= threshold:
            return min_divisor
        if self.get_divide_result_sum(nums, max_divisor) <= threshold:
            return max_divisor

        return max_divisor

    def get_divide_result_sum(self, nums: List[int], divisor: int):
        sum_of_division_results = 0
        for num in nums:
            sum_of_division_results += ceil(num / divisor)

        return sum_of_division_results
