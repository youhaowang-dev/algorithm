// Array, Backtracking
// Airbnb 4 Reddit 4 Amazon 2 Facebook 5 Bloomberg 4 Google 2 Microsoft 2 Oracle 2 ByteDance 2 Uber 3 eBay 3 LinkedIn 2 Apple 2 TikTok 2 Snapchat
// https://leetcode.com/problems/combination-sum-ii/
// Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

// Each number in candidates may only be used once in the combination.

// Note: The solution set must not contain duplicate combinations.

// Example 1:
// Input: candidates = [10,1,2,7,6,1,5], target = 8
// Output:
// [
// [1,1,6],
// [1,2,5],
// [1,7],
// [2,6]
// ]
// Example 2:
// Input: candidates = [2,5,2,1,2], target = 5
// Output:
// [
// [1,2,2],
// [5]
// ]
class CombinationSumII {

  // Time complexity is O(2^n). Space complexity O(n). Basically, for each num you have two choices, pick it or not.
  public List<List<Integer>> combinationSum2(int[] nums, int target) {
    List<List<Integer>> result = new ArrayList<>();
    if (nums == null || nums.length == 0) {
      return result;
    }

    int targetRemain = target - 0;
    List<Integer> list = new ArrayList<>(); // track the state of nums
    int startIndex = 0; // not reuse number
    // To remove dups, for example, 1,2a,2b,5, to get 7, cur pointer is on 1, then 1, 2a, 5, and 1, 2b, 5, would be dups.
    // select multi values, for example 1,2,2, it will be covered when cur pointer is 2a
    Arrays.sort(nums);
    this.combinationSum2Helper(nums, targetRemain, result, list, startIndex);

    return result;
  }

  private void combinationSum2Helper(
    int[] nums,
    int targetRemain,
    List<List<Integer>> result,
    List<Integer> list,
    int startIndex
  ) {
    // exit
    if (targetRemain < 0) {
      return;
    }

    if (targetRemain == 0) {
      result.add(new ArrayList<Integer>(list));
      return;
    }
    // remain > 0
    // continue search
    for (int i = startIndex; i < nums.length; i++) {
      // dedup for non-first number as the first number should not be skipped
      // i > startIndex is for NOT skipping the first number as it should always be picked
      // i > startIndex also handles edge cases where i == 0
      if (i > startIndex && nums[i] == nums[i - 1]) {
        continue;
      }

      list.add(nums[i]);
      this.combinationSum2Helper(
          nums,
          targetRemain - nums[i],
          result,
          list,
          i + 1
        );
      list.remove(list.size() - 1);
    }
  }
}
