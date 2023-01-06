# https://www.lintcode.com/problem/463/
# Given an integer array, sort it in ascending order. Use selection sort, bubble sort, insertion sort or any O(n2) algorithm.
from ast import List


class SortIntegers:
    def sort_integers(self, nums: List[int]) -> None:
        self.selection_sort(nums)
        # self.bubble_sort(nums)
        # self.insertion_sort(nums)

    # selection sort: select min in each loop, swap it to head
    def selection_sort(self, nums: List[int]) -> None:
        for i in range(0, len(nums)):
            minIndex = self.get_min_index(nums, i)
            self.swap(nums, minIndex, i)

    def get_min_index(self, nums: List[int], start: int) -> None:
        minIndex = start
        min = nums[start]
        for i in range(start, len(nums)):
            if min > nums[i]:
                minIndex = i
                min = nums[i]

        return minIndex

    # bubble sort: repeatedly swapping the adjacent elements if they are in the wrong order
    def bubble_sort(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(0, n - 1):
            sorted = True  # optional
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    self.swap(nums, j, j + 1)
                    sorted = False
            if sorted:
                break

    def swap(self, nums: List[int], a: int, b: int) -> None:
        numACopy = nums[a]
        nums[a] = nums[b]
        nums[b] = numACopy

    def insertion_sort(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            current = nums[i]
            j = i - 1

            # Move elements of nums[0..i-1], that are greater than current, to one position ahead of their current position
            while j >= 0 and nums[j] > current:
                nums[j + 1] = nums[j]
                j = j - 1

            nums[j + 1] = current
