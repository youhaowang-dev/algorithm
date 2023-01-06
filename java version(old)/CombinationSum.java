// Array, Backtracking
// Airbnb 9 Amazon 5 eBay 4 Google 3 Adobe 3 Microsoft 3 Apple 3 Facebook 2 Walmart Global Tech 2 Reddit 2 Bloomberg 9 ByteDance 5 LinkedIn 4 Goldman Sachs 2 Zillow 2 Oracle 2 TikTok 2 Snapchat 4 Uber 4 Salesforce 3 Cisco 2 Arcesium 2
// https://leetcode.com/problems/combination-sum/

// Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

// The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
// frequency
//  of at least one of the chosen numbers is different.

// The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

// Example 1:
// Input: candidates = [2,3,6,7], target = 7
// Output: [[2,2,3],[7]]
// Explanation:
// 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
// 7 is a candidate, and 7 = 7.
// These are the only two combinations.
// Example 2:
// Input: candidates = [2,3,5], target = 8
// Output: [[2,2,2,2],[2,3,3],[3,5]]
// Example 3:
// Input: candidates = [2], target = 1
// Output: []

class CombinationSum {

  // time O(nums_count^(target/min_num)) => O(N^(T/M))
  // each number will fanout O(target/min_num) searches recursively, and each search cost bounded by O(nums_count)
  // space O(target/min_num)
  public List<List<Integer>> combinationSum(int[] nums, int target) {
    List<List<Integer>> result = new ArrayList<>();
    int sum = 0;
    List<Integer> list = new ArrayList<>();
    int startIndex = 0;
    int targetRemain = target - 0;
    this.combinationSumHelper(nums, targetRemain, result, list, startIndex);

    return result;
  }

  private void combinationSumHelper(
    int[] nums,
    int targetRemain,
    List<List<Integer>> result,
    List<Integer> list,
    int startIndex
  ) {
    if (targetRemain < 0) {
      return;
    }

    if (targetRemain == 0) {
      result.add(new ArrayList<Integer>(list));
    }

    // targetRemain > 0
    for (int i = startIndex; i < nums.length; i++) {
      list.add(nums[i]);
      this.combinationSumHelper(nums, targetRemain - nums[i], result, list, i); // i for reuse current number
      list.remove(list.size() - 1);
    }
  }
}
