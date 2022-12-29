// Array, Backtracking, Bit Manipulation
// Amazon 5 Google 2 Yahoo 2 Bloomberg 4 Facebook 3 Adobe 3 Apple 3 Uber 2 TikTok 2
// https://leetcode.com/problems/subsets-ii/

// Given an integer array nums that may contain duplicates, return all possible
// subsets(the power set).

// The solution set must not contain duplicate subsets. Return the solution in any order.

// Example 1:
// Input: nums = [1,2,2]
// Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
// Example 2:
// Input: nums = [0]
// Output: [[],[0]]

class SubsetsII {

  // time O(n * 2^n) generate all subsets and then copy them into output list
  // space O(n * 2^n) This is exactly the number of solutions for subsets multiplied by the number N of elements to keep for each subset.
  // For a given number, it could be present or absent (i.e. binary choice) in a subset solution.
  // As as result, for N numbers, we would have in total 2^N choices (solutions).

  // use set to dedup
  public List<List<Integer>> subsetsWithDup(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();
    // sort is need for dedup because same number need to be ordered
    // For example input is {2,1,2}. In the backtrack we can have {2,1} and {1, 2}.
    // And HashSet will treat this both as new elements, whereas both are same just order is different.
    // So avoid this we sort here first. Making the list {1,2,2}. So in the backtrack we will get {1,2} and {1,2}. But set will discard the second {1,2}.
    Arrays.sort(nums);

    Deque<Integer> subset = new ArrayDeque<>();
    Set<List<Integer>> resultSet = new HashSet<>();
    this.subsetsHelper(nums, 0, subset, resultSet);

    return new ArrayList<>(resultSet);
  }

  private void subsetsHelper(
    int[] nums,
    int startIndex, // this is needed for subset is unordered, so each number should only be picked once
    Deque<Integer> subset,
    Set<List<Integer>> resultSet
  ) {
    resultSet.add(new ArrayList<Integer>(subset));

    for (int i = startIndex; i < nums.length; i++) {
      subset.addLast(nums[i]);
      this.subsetsHelper(nums, i + 1, subset, resultSet);
      subset.removeLast();
    }
  }

  // not using set to dedup
  public List<List<Integer>> subsetsWithDup(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();
    // sort is need for dedup
    Arrays.sort(nums);

    Deque<Integer> subset = new ArrayDeque<>();
    this.subsetsHelper(nums, 0, subset, result);

    return result;
  }

  private void subsetsHelper(
    int[] nums,
    int start,
    Deque<Integer> subset,
    List<List<Integer>> result
  ) {
    result.add(new ArrayList<Integer>(subset));
    for (int i = start; i < nums.length; i++) {
      if (i != start && nums[i] == nums[i - 1]) {
        continue;
      }
      subset.addLast(nums[i]);
      this.subsetsHelper(nums, i + 1, subset, result);
      subset.removeLast();
    }
  }
}
