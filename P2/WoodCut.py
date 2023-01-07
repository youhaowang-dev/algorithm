# https://www.lintcode.com/problem/183/description
# Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee
# you could have equal or more than k pieces with the same length. What is the longest length you
# can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

# Example 1
# Input:
# L = [232, 124, 456]
# k = 7
# Output: 114
# Explanation: We can cut it into 7 pieces if any piece is 114 long, however we can't cut it into 7 pieces
# if any piece is 115 long. And for the 124 logs, the excess can be discarded and not used in its entirety.

# Example 2
# Input:
# L = [1, 2, 3]
# k = 7
# Output: 0
# Explanation: It is obvious we can't make it.

# Challenge
# O(n log Len), where Len is the longest length of the wood.

from ast import List

# linear search for a max, so decrease max cut len while cut_count > min_cut_count
# return when first time the cut is too small: cut_count <= min_cut_count
class WoodCut:
    def wood_cut(self, wood_lengths: List[int], min_cut_count: int) -> int:
        if not wood_lengths:
            return 0

        max_cut_length = max(wood_lengths)
        min_cut_length = 1
        while min_cut_length + 1 < max_cut_length:
            cut_count = self.get_cut_count(wood_lengths, max_cut_length)
            if cut_count >= min_cut_count:
                return max_cut_length
            else:
                max_cut_length -= 1

        if min_cut_count >= self.get_cut_count(wood_lengths, max_cut_length):
            return max_cut_length
        if min_cut_count >= self.get_cut_count(wood_lengths, min_cut_length):
            return min_cut_length

        return 0

    def get_cut_count(self, wood_lengths: List[int], cut_length: int) -> int:
        cut_count = 0
        for wood_length in wood_lengths:
            ## // because we only need cut_length woods
            cut_count += wood_length // cut_length

        return cut_count


class WoodCut2:
    def wood_cut(self, wood_lengths: List[int], min_cut_count: int) -> int:
        if not wood_lengths:
            return 0

        max_cut_length = max(wood_lengths)
        min_cut_length = 1
        while min_cut_length + 1 < max_cut_length:
            cut_length = (min_cut_length + max_cut_length) // 2
            cut_count = self.get_cut_count(wood_lengths, cut_length)
            if cut_count == min_cut_count:
                min_cut_length = cut_length
            if cut_count > min_cut_count:
                # make cut smaller to get less cut count to find the max
                min_cut_length = cut_length
            if cut_count < min_cut_count:
                # make cut bigger to get more cut count
                max_cut_length = cut_length

        if self.get_cut_count(wood_lengths, max_cut_length) >= min_cut_count:
            return max_cut_length
        if self.get_cut_count(wood_lengths, min_cut_length) >= min_cut_count:
            return min_cut_length

        return 0

    def get_cut_count(self, wood_lengths: List[int], cut_length: int):
        cut_count = 0
        for wood_length in wood_lengths:
            cut_count += wood_length // cut_length

        return cut_count
