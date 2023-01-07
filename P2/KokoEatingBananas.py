# Array, Binary Search
# Amazon 13 Google 4 DoorDash 4 Salesforce 4 Bloomberg 3 Arcesium 3 eBay 2 Facebook 6 Airbnb 4 Apple 4 Uber 2 TikTok 2 Adobe 2 epiFi 2
# https://leetcode.com/problems/koko-eating-bananas/

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23

from ast import List
from math import ceil


# brute force: linear search the speed from min to max
class KokoEatingBananas:
    def minEatingSpeed(self, piles: List[int], max_eat_hour: int) -> int:
        min_eat_speed = 1
        max_eat_speed = max(piles)
        while min_eat_speed + 1 < max_eat_speed:
            eat_hour = self.get_eat_hour(piles, min_eat_speed)
            if eat_hour > max_eat_hour:
                min_eat_speed += 1
            else:
                return min_eat_speed

        return max_eat_speed

    def get_eat_hour(self, piles: List[int], eat_speed: int) -> int:
        eat_hour = 0
        for pile in piles:
            eat_hour += ceil(pile / eat_speed)

        return eat_hour


# binary search the min eat speed
# time O(pile_count * log(max_pile)) + get max pile O(log(pile_count)) => O(mlogn) where m=pile_count,n=max_pile
class KokoEatingBananas2:
    def minEatingSpeed(self, piles: List[int], max_eat_hour: int) -> int:
        min_eat_speed = 1
        max_eat_speed = max(piles)
        while min_eat_speed + 1 < max_eat_speed:
            eat_speed = (min_eat_speed + max_eat_speed) // 2
            eat_hour = self.get_eat_hour(piles, eat_speed)

            if eat_hour > max_eat_hour:
                min_eat_speed = eat_speed
            if eat_hour < max_eat_hour:
                max_eat_speed = eat_speed
            if eat_hour == max_eat_hour:
                max_eat_speed = eat_speed  # make it smaller
                # return eat_speed # we are searching min, so cannot do this

        if self.get_eat_hour(piles, min_eat_speed) <= max_eat_hour:
            return min_eat_speed

        if self.get_eat_hour(piles, max_eat_speed) <= max_eat_hour:
            return max_eat_speed

        return -1  # throw

    def get_eat_hour(self, piles: List[int], eat_speed: int) -> int:
        eat_hour = 0
        for pile in piles:
            eat_hour += ceil(pile / eat_speed)

        return eat_hour
