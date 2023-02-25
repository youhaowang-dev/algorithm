#
# Facebook 19 Google 15 Roblox 4 Uber 11 Amazon 10 LinkedIn 9 Microsoft 6 Twitter 2 Apple 2 Yelp 7 Bloomberg 6
# Two Sigma 4 ByteDance 4 Snapchat 3 Expedia 3 Adobe 3 instacart 3 Cruise Automation 2 TikTok 2 Rubrik
# https://leetcode.com/problems/random-pick-with-weight/

# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

# You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

# Example 1:
# Input
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output
# [null,0]
# Explanation
# Solution solution = new Solution([1]);
# solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
from random import random
from typing import List

# prefix sum + linear search
class RandomPickwithWeight:
    def __init__(self, w: List[int]):
        self.prefix_sums = list()
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()

        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i


# prefix sum + binary search(positive integers, so prefix sums are increasing)
class RandomPickwithWeight2:
    def __init__(self, w: List[int]):
        self.prefix_sums = list()
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        left = 0
        right = len(self.prefix_sums)
        while left < right:
            mid = left + (right - left) // 2
            if target > self.prefix_sums[mid]:
                left = mid + 1
            else:
                right = mid

        return left


import collections

Box = collections.namedtuple("Box", ("small", "big", "div"))

# O(1)
class RandomPickwithWeight3:
    def __init__(self, w):
        self.n, self.size = len(w), sum(w)
        self.boxes = []
        w = [elem * self.n for elem in w]
        bigs = {i: x for i, x in enumerate(w) if x >= self.size}
        smalls = {i: x for i, x in enumerate(w) if x < self.size}
        while smalls:
            big = next(iter(bigs))
            small, div = smalls.popitem()
            self.boxes.append(Box(small, big, div))
            bigs[big] -= self.size - div
            if bigs[big] < self.size:
                smalls[big] = bigs.pop(big)
        self.boxes += [Box(0, big, 0) for big in bigs]

    def pickIndex(self):
        box = random.choice(self.boxes)
        weight = random.randint(0, self.size)
        return box.big if weight >= box.div else box.small
