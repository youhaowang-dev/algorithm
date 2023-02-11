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

# time complexity = O(C(n,k) * k) = O((n!/(k! * (n - k)!)) * k)
# copy list takes O(k), so C(n,k) * k.
class Combinations:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < k or k == 0:
            return list()

        results = list()
        result = list()
        n_start = 1
        self.search_result(n, k, n_start, result, results)

        return results

    def search_result(self, n, k, n_start, result, results):
        if len(result) == k:
            results.append(list(result))
            return

        for i in range(n_start, n + 1):
            result.append(i)
            self.search_result(n, k, i + 1, result, results)
            result.pop()
