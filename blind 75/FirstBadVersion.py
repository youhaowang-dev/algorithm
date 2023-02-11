# Binary Search, Interactive
# Google 8 Amazon 8 Adobe 7 Apple 6 Microsoft 3 Facebook 2 Uber 2 Yahoo 2 VMware 2 Bloomberg 2 Expedia 2 Cisco 2 Oracle 2 Goldman Sachs 2
# https://leetcode.com/problems/first-bad-version/
# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Example 1:
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

# Example 2:
# Input: n = 1, bad = 1
# Output: 1

# 1,2,3,4,5,6 and 3 is the first bad version
# l   m     r       m is bad version, drop right side [m+1, r] because target(first bad version) is not in this part
# l m r             m is not bad, drop [l, m] as this part does not have the target(first bad version)
#   l r             exit loop; check left first, then right
class FirstBadVersion:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left + 1 < right:  # never infinite loop
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid  # search the leftmost of bad
            else:
                left = mid

        if isBadVersion(left):
            return left

        return right
