// Array, Backtracking
// Amazon 15 Microsoft 4 Bloomberg 3 Adobe 3 Google 2 Yahoo 2 Walmart Global Tech 2 Citadel 2 Uber 2 Facebook 7 LinkedIn 4 Apple 4 TikTok 3 Paypal 2 Goldman Sachs 2 GoDaddy 2 Nvidia 2 Visa 2 eBay 6 Oracle 4 ByteDance 4 Snapchat 2 PayTM 2
// https://leetcode.com/problems/permutations/

// Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

// Example 1:
// Input: nums = [1,2,3]
// Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
// Example 2:
// Input: nums = [0,1]
// Output: [[0,1],[1,0]]
// Example 3:
// Input: nums = [1]
// Output: [[1]]
class Permutations {

  public List<List<Integer>> permute(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();
    if (nums == null || nums.length == 0) {
      return null;
    }

    List<Integer> list = new ArrayList<>(); // the permutation state
    boolean[] used = new boolean[nums.length]; // for avoid contains O(n)
    this.permuteHelper(nums, list, used, result);

    return result;
  }

  // permutation is ordered, so no start index is needed to dedup
  // [1,2,3] !=[1,3,2]
  private void permuteHelper(
    int[] nums,
    List<Integer> list,
    boolean[] used,
    List<List<Integer>> result
  ) {
    if (list.size() == nums.length) {
      result.add(new ArrayList<Integer>(list));
      return;
    }

    for (int i = 0; i < nums.length; i++) {
      if (used[i]) {
        continue;
      }
      list.add(nums[i]);
      used[i] = true;
      this.permuteHelper(nums, list, used, result);
      list.remove(list.size() - 1);
      used[i] = false;
    }
  }
}
