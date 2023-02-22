# Array, Backtracking
# LinkedIn 2 Amazon 2 Microsoft 3 Google 2 Bloomberg 2 Apple 2 Facebook 3 Adobe 3 Oracle 2
# https://leetcode.com/problems/permutations-ii/description/

# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# worse case is no duplication
# n*n! each choice will reduce next choice count by 1, copy and hash takes n
class PermutationsII:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return list()

        num_to_count = collections.Counter(nums)
        results = list()
        result = list()
        self.build_results(results, result, num_to_count, len(nums))

        return results

    def build_results(self, results, result, num_to_count, expected_result_length):
        if len(result) == expected_result_length:
            results.append(list(result))
            return

        for num in num_to_count.keys():
            if num_to_count[num] == 0:
                continue

            result.append(num)
            num_to_count[num] -= 1
            self.build_results(results, result, num_to_count,
                               expected_result_length)
            num_to_count[num] += 1
            result.pop()

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return list()

        results = set()  # Set[Tuple[int]]
        result = list()
        used = set()
        self.build_results(nums, results, result, used)
        # return list(map(list, results))
        return results

    def build_results(self, nums, results, result, used):
        if len(result) == len(nums):
            results.add(tuple(result))
            return

        for i, num in enumerate(nums):
            if i in used:
                continue

            result.append(num)
            used.add(i)
            self.build_results(nums, results, result, used)
            result.pop()
            used.remove(i)
