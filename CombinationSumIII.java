// Array, Backtracking
// Google 3 Amazon 3 Adobe 2 Microsoft 2 Expedia 2 Apple 2
// https://leetcode.com/problems/combination-sum-iii/
// Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

// Only numbers 1 through 9 are used.
// Each number is used at most once.
// Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

// Example 1:
// Input: k = 3, n = 7
// Output: [[1,2,4]]
// Explanation:
// 1 + 2 + 4 = 7
// There are no other valid combinations.
// Example 2:
// Input: k = 3, n = 9
// Output: [[1,2,6],[1,3,5],[2,3,4]]
// Explanation:
// 1 + 2 + 6 = 9
// 1 + 3 + 5 = 9
// 2 + 3 + 4 = 9
// There are no other valid combinations.
// Example 3:
// Input: k = 4, n = 1
// Output: []
// Explanation: There are no valid combinations.
// Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
class CombinationSumIII {

  // time complexity O(9^k) as we evaluate part of all the subsets
  // space O(k) for maintaining the state list and recursion tree depth can be max k
  public List<List<Integer>> combinationSum3(int targetSize, int target) {
    List<List<Integer>> result = new ArrayList<>();
    List<Integer> list = new ArrayList<>(); // nums state
    int targetRemain = target - 0;
    int startNum = 1;

    this.combinationSum3Helper(
        targetSize,
        targetRemain,
        startNum,
        list,
        result
      );

    return result;
  }

  private void combinationSum3Helper(
    int targetSize,
    int targetRemain,
    int startNum,
    List<Integer> list,
    List<List<Integer>> result
  ) {
    if (targetRemain == 0 && list.size() == targetSize) {
      result.add(new ArrayList<Integer>(list));
      return;
    }

    if (targetRemain < 0) {
      return;
    }

    if (list.size() == targetSize) {
      return;
    }

    for (int number = startNum; number < 10; number++) {
      list.add(number);
      this.combinationSum3Helper(
          targetSize,
          targetRemain - number,
          number + 1,
          list,
          result
        );
      list.remove(list.size() - 1);
    }
  }
}
