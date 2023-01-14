from typing import List


# dict O(n) space and time
class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = dict()
        for i, num in enumerate(nums):
            target_remain = target - num
            if target_remain in num_to_index:
                return [i, num_to_index.get(target_remain)]

            num_to_index[num] = i

        return [-1, -1]


# brute force O(n^2) time O(1) space
class TwoSum2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        # i and j are indexes of nums
        for i in range(0, length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [-1, -1]
