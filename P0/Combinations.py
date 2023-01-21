# Backtracking
# Bloomberg 2 Yahoo 2 Facebook 4 Microsoft 3 Google 2 Amazon 6 Apple 4 Adobe 2 Huawei 2
# https://leetcode.com/problems/combinations/
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.


from ast import List


class Combinations:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = list()
        if n < k or n < 1:
            return result

        n_start = 1
        combine_state = list()
        self.combine_helper(n, k, n_start, combine_state, result)

        return result

    def combine_helper(self, n, k, n_start, combine_state, result):
        if k == 0:
            result.append(list(combine_state))

        for i in range(n_start, n + 1):
            combine_state.append(i)
            self.combine_helper(n, k - 1, i + 1, combine_state, result)
            combine_state.pop()
