// Array, Backtracking
// LinkedIn 2 Amazon 2 Microsoft 3 Google 2 Bloomberg 2 Apple 2 Facebook 3 Adobe 3 Oracle 2
// https://leetcode.com/problems/permutations-ii/description/

// Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

// Example 1:
// Input: nums = [1,1,2]
// Output:
// [[1,1,2],
//  [1,2,1],
//  [2,1,1]]
// Example 2:
// Input: nums = [1,2,3]
// Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class PermutationsII {

  public List<List<Integer>> permuteUnique(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();
    if (nums == null || nums.length == 0) {
      return null;
    }

    Arrays.sort(nums);

    Deque<Integer> list = new ArrayDeque<>(); // the permutation state
    boolean[] used = new boolean[nums.length]; // for avoid contains O(n)
    this.permuteHelper(nums, list, result, used);

    return result;
  }

  private void permuteHelper(
    int[] nums,
    Deque<Integer> list,
    List<List<Integer>> result,
    boolean[] used
  ) {
    if (list.size() == nums.length) {
      result.add(new ArrayList<>(list));
      return;
    }

    for (int i = 0; i < nums.length; i++) {
      if (used[i]) {
        continue;
      }
      if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
        continue;
      }
      list.add(nums[i]);
      used[i] = true;
      this.permuteHelper(nums, list, result, used);
      list.removeLast();
      used[i] = false;
    }
  }
}
