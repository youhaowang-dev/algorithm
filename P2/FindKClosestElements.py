# Array, Two Pointers, Binary Search, Sliding Window, Sorting, Heap (Priority Queue)
# Amazon 8 Adobe 5 DoorDash 3 Google 2 Facebook 2 Bloomberg 2 Apple 2 TikTok 2 Uber 2 Oracle 2 Microsoft 13 Paypal 4 LinkedIn 2 Goldman Sachs 2 ByteDance 2
# https://leetcode.com/problems/find-k-closest-elements/description/

# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b

# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]

from ast import List

# search A[left] < target, A[right] >= target => expand left and right => build result
# time: O(logn + 2k)
class FindKClosestElements:
    def findClosestElements(self, nums: List[int], k: int, target: int) -> List[int]:
        # get the two neighbors that are closest to target
        # A[left] < target, A[right] >= target
        right = self.find_upper_closest(nums, target)
        left = right - 1

        for _ in range(0, k):
            if self.is_left_closer(nums, target, left, right):
                left -= 1
            else:
                right += 1

        # left could be -1 and right could be length
        result = []
        for i in range(left + 1, right):
            result.append(nums[i])

        return result

    def find_upper_closest(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid

        if nums[left] >= target:
            return left

        if nums[right] >= target:
            return right

        return len(nums)  # not found

    def is_left_closer(
        self, nums: List[int], target: int, left: int, right: int
    ) -> bool:
        if left < 0:
            return False

        if right >= len(nums):
            return True

        return (target - nums[left]) <= (nums[right] - target)


# sort and slice and sort again
# time O(N⋅log(N)+k⋅log(k))
# space O(N)
class FindKClosestElements2:
    def findClosestElements(self, nums: List[int], k: int, target: int) -> List[int]:
        compare_function = lambda num: abs(target - num)
        sortedByDistance = sorted(nums, key=compare_function)

        return sorted(sortedByDistance[0:k])


# two pointers O(n)
class FindKClosestElements3:
    def findClosestElements(self, nums: List[int], k: int, target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while right - left >= k:
            if abs(nums[left] - target) > abs(nums[right] - target):
                left += 1
            else:
                right -= 1

        result = []
        for i in range(left, right + 1):
            result.append(nums[i])

        return result


# binary search time O(log(N−k)+k) space O(1)
# right is bounded by length - k, so left=0 and right=len-k
# compare (target - nums[mid]) and (nums[mid+k] - target)
# At the end of the binary search, we have located the leftmost index for the final answer.
class FindKClosestElements4:
    def findClosestElements(self, nums: List[int], k: int, target: int) -> List[int]:
        left = 0
        right = len(nums) - k

        while left < right:
            mid = (left + right) // 2
            if target - nums[mid] > nums[mid + k] - target:
                left = mid + 1
            else:
                right = mid

        result = []
        for i in range(left, left + k):
            result.append(nums[i])

        return result
