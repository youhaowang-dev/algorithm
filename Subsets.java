// Array, Backtracking, Bit Manipulation
// Amazon 10 Bloomberg 8 Facebook 2 Apple 2 Google 2 icrosoft 4 Adobe 4 TikTok 4 Uber 3 Twitter 3 Reddit 3 Oracle 2 Walmart Global Tech 2 Visa 2 ByteDance 9 Goldman Sachs 6 Yahoo 2 Paypal 2 eBay 2 Coupang
// https://leetcode.com/problems/subsets/description/

// Given an integer array nums of unique elements, return all possible
// subsets
//  (the power set).

// The solution set must not contain duplicate subsets. Return the solution in any order.

// Example 1:
// Input: nums = [1,2,3]
// Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
// Example 2:
// Input: nums = [0]
// Output: [[],[0]]
class Subsets {

  // time O(n * 2^n) generate all subsets and then copy them into output list
  // space O(n * 2^n) This is exactly the number of solutions for subsets multiplied by the number N of elements to keep for each subset.
  // For a given number, it could be present or absent (i.e. binary choice) in a subset solution.
  // As as result, for N numbers, we would have in total 2^N choices (solutions).
  public List<List<Integer>> subsets(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();
    // sort is optional for input has no dup, so no need to dedup
    // Arrays.sort(nums);
    Deque<Integer> subset = new ArrayDeque<>(); // state in dfs
    this.subsetsHelper(nums, 0, subset, result);

    return result;
  }

  // dfs
  private void subsetsHelper(
    int[] nums,
    int startIndex,
    Deque<Integer> subset,
    List<List<Integer>> result
  ) {
    result.add(new ArrayList<Integer>(subset));
    for (int i = startIndex; i < nums.length; i++) {
      subset.addLast(nums[i]);
      this.subsetsHelper(nums, i + 1, subset, result);
      subset.removeLast();
    }
  }
}
