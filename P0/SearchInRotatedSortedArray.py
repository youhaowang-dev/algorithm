# Array, Binary Search, Divide and Conquer
# Amazon 21 Bloomberg 10 Microsoft 7 Apple 7 Adobe 5 Media.net 5 Facebook 4 LinkedIn 4 Uber 3 Yahoo 2 Google 2 TikTok 2
# https://leetcode.com/problems/search-in-rotated-sorted-array/
#     There is an integer array nums sorted in ascrighting order (with distinct values).
#     Prior to being passed to your function, nums is possibly rotated at an unknown pivot
#     index k (1 <= k < len(nums)) such that the resulting array is
#     [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
#     For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#     Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
#     You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1

from ast import List

# brute force: linear scan O(n)


class SearchInRotatedSortedArray:

    # binary search O(logn)
    # 4,5,6,7,0,1,2
    # l t   m     r      => left sorted and t in left           => r move to m
    # l     m   t r      => left sorted but t not in left       => l move to m
    # 4,5,6,7,0,1,2
    #   l t   m   r      => right sorted but t not in right     => r move to m
    #   l     m t r      => right sorted and t in right         => l move to m
    # mid can split the rotated array in two parts
    #  one part is sorted, the other part is unsorted
    # handle the sorted part by additionaly checking if the target in this part
    # if sorted part contains the target, continue search in this part
    # if sorted part does not contain the target, continue search the other part
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left - (left - right) // 2
            midVal = nums[mid]
            leftVal = nums[left]
            rightVal = nums[right]
            # handle equals
            if midVal == target:
                return mid
            if leftVal == target:
                return left
            if rightVal == target:
                return right

            # handle sorted
            leftPartSorted = leftVal < midVal
            targetInLeftPart = leftVal < target and target < midVal
            if leftPartSorted:
                if targetInLeftPart:
                    right = mid
                else:
                    left = mid

            rightPartSorted = midVal < rightVal
            targetInRightPart = midVal < target and target < rightVal
            if rightPartSorted:
                if targetInRightPart:
                    left = mid
                else:
                    right = mid
        # left + 1 == right:
        if nums[left] == target:
            return left

        if nums[right] == target:
            return right

        return -1


class SearchInRotatedSortedArray2:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1

        search = BinarySearchTarget(nums, target)
        while search.unfinished():
            targetFound = search.targetFound()
            if targetFound is not None:
                return targetFound
            search.updateLeftPart()
            search.updateRightPart()

        if search.getLeftVal() == target:
            return search.left

        if search.getRightVal() == target:
            return search.right

        return -1


# TODO: private attributes and methods
class BinarySearchTarget:
    def __init__(self, nums: List[int], target: int):
        self.left = 0
        self.right = len(nums) - 1
        self.target = target
        self.nums = nums

    def unfinished(self) -> bool:
        return self.left + 1 < self.right

    def targetFound(self):  # TODO: add type
        if self.getMidVal() == self.target:
            return self.getMid()
        if self.getLeftVal() == self.target:
            return self.left
        if self.getRightVal() == self.target:
            return self.right

        return None

    def updateLeftPart(self) -> None:
        if self.leftPartSorted():
            if self.targetInLeftPart():
                self.right = self.getMid()
            else:
                self.left = self.getMid()

    def updateRightPart(self) -> None:
        if self.rightPartSorted():
            if self.targetInRightPart():
                self.left = self.getMid()
            else:
                self.right = self.getMid()

    def getLeftVal(self) -> int:
        return self.nums[self.left]

    def getRightVal(self) -> int:
        return self.nums[self.right]

    def getMidVal(self) -> int:
        return self.nums[self.getMid()]

    def getMid(self) -> int:
        return self.left + (self.right - self.left) // 2

    def leftPartSorted(self) -> bool:
        return self.getLeftVal() < self.getMidVal()

    def targetInLeftPart(self) -> bool:
        return self.getLeftVal() < self.target and self.target < self.getMidVal()

    def rightPartSorted(self) -> bool:
        return self.getMidVal() < self.getRightVal()

    def targetInRightPart(self) -> bool:
        return self.getMidVal() < self.target and self.target < self.getRightVal()


class SearchInRotatedSortedArray3:
    # 1. binary search the min index
    # 2. binary search the target in the sorted part
    def search(self, nums: List[int], target: int) -> int:
        if nums is None and len(nums) == 0:
            return -1

        minIndex = self.find_min_index(nums)
        # if min is -1, that means the array is not rotated, the following code still works
        rightVal = nums[len(nums) - 1]
        if target == rightVal:
            return len(nums) - 1

        targetInLeftPart = target > rightVal
        left = 0 if targetInLeftPart else minIndex
        right = minIndex - 1 if targetInLeftPart else len(nums) - 1
        while left + 1 < right:
            mid = left - (left - right) // 2
            midVal = nums[mid]
            if midVal == target:
                return mid
            if midVal < target:
                left = mid
            if midVal > target:
                right = mid

        # if not found, index could go out of bound
        if left >= 0 and left <= len(nums) - 1 and nums[left] == target:
            return left
        if right >= 0 and right <= len(nums) - 1 and nums[right] == target:
            return right

        return -1

    def find_min_index(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left - (left - right) // 2
            midVal = nums[mid]
            rightVal = nums[right]
            if midVal < rightVal:
                right = mid
            if midVal > rightVal:
                left = mid
            # assumed no dup

        if nums[left] < nums[right]:
            return left

        if nums[left] > nums[right]:
            return right

        return -1
