# Array, Prefix Sum
# Amazon 16 Apple 6 Bloomberg 6 Microsoft 4 Adobe 4 Facebook 3 Walmart Global Tech 3 American Express 3
# Google 2 Uber 2 Salesforce 2 DE Shaw 2 Asana 14 Lyft 3 Yahoo 3 Oracle 3 Groupon 2 Qualtrics 2 TikTok 2 IBM 2
# Paypal 5 Goldman Sachs 5 Intel 4 Expedia 3 VMware 3 Nutanix 2 Nvidia 2 ServiceNow 2 Indeed 2 Arista Networks 2
# PayTM 2 MakeMyTrip 2 Zillow 2 LinkedIn
# https://leetcode.com/problems/product-of-array-except-self/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Follow up: Can you solve the problem in O(1) extra space complexity?
# (The output array does not count as extra space for space complexity analysis.)

# brute force: product of all for each index and divide self
# keep track of leftProduct and rightProduct
# two passes to build the result
# time n, space 1 output does not count
# [1, 0, 0, 0] => [1, 1, 0, 0] => [1, 1, 2, 0] => [1, 1, 2, 6]
# [1, 1, 2, 6] => [1, 1, 8, 6] => [1, 12, 8, 6] => [24, 12, 8, 6]
class ProductOfArrayExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return list()

        length = len(nums)
        products = [0 for _ in range(length)]

        prefix_product = 1
        for i in range(0, length):
            products[i] = prefix_product
            prefix_product = prefix_product * nums[i]

        suffix_product = 1
        for i in range(length - 1, -1, -1):
            products[i] = products[i] * suffix_product
            suffix_product = suffix_product * nums[i]

        return products


# preprocess data from both ends
# multiply from left and multiply from right
# so for an index we can easily find the left and right products
# time n space n
class ProductOfArrayExceptSelf2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0
        length = len(nums)

        # build left products
        leftProducts = [0 for _ in range(0, length)]
        leftProducts[0] = nums[0]
        for i in range(1, len(nums)):
            leftProducts[i] = nums[i] * leftProducts[i - 1]

        # build right products
        rightProducts = [0 for _ in range(0, length)]
        rightProducts[length - 1] = nums[length - 1]
        for i in range(len(nums) - 2, 0, -1):
            rightProducts[i] = nums[i] * rightProducts[i + 1]

        # build result
        result = [0 for _ in range(0, length)]
        result[0] = rightProducts[1]
        result[length - 1] = leftProducts[length - 1 - 1]
        for i in range(1, length - 1):
            leftProduct = leftProducts[i - 1]
            rightProduct = rightProducts[i + 1]
            result[i] = leftProduct * rightProduct

        return result
