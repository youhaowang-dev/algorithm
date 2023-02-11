# Array, Two Pointers, Sorting
# Amazon 12 Apple 6 Microsoft 5 Yahoo 3 ServiceNow 3 Google 2 Bloomberg 2 VMware 2 Adobe 2 Uber 4 Facebook 4
# Salesforce 3 Nvidia 3 Grab 3 Walmart Global Tech 2 Samsung 2 Intel 2 Oracle 2 eBay 2 Visa 2 Spotify 2 Swiggy 2 Tesla 2 Sprinklr 2 Pocket Gems
# https://leetcode.com/problems/sort-colors/description/

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that
# objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

# brute force: counting sort
# one pass: swap 0 to left and 2 to right, so 1 is in the middle
# three pointers to track the tail of 0, the head of 2, and the current swap position
class SortColors:
    def sortColors(self, nums: List[int]) -> None:
        if not nums:
            return

        zero_tail = 0
        two_head = len(nums) - 1
        current = 0
        while current <= two_head:
            if nums[current] == 0:
                nums[current], nums[zero_tail] = nums[zero_tail], nums[current]
                zero_tail += 1
                current += 1
            elif nums[current] == 2:
                nums[current], nums[two_head] = nums[two_head], nums[current]
                two_head -= 1
                # dont move current as current can be 0 or 1
            elif nums[current] == 1:  # noop
                current += 1


class SortColors2:  # two passes
    def sortColors(self, nums: List[int]) -> None:
        if not nums:
            return
        length = len(nums)

        zero_tail = 0
        current = zero_tail
        while current < length:
            if nums[current] == 0:
                nums[current], nums[zero_tail] = nums[zero_tail], nums[current]
                zero_tail += 1
                current += 1
            else:
                current += 1

        two_head = length - 1
        current = two_head
        while current >= 0:
            if nums[current] == 2:
                nums[current], nums[two_head] = nums[two_head], nums[current]
                two_head -= 1
                current -= 1
            else:
                current -= 1
