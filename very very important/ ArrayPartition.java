// Array, Greedy, Sorting, Counting Sort
// Adobe 2 Amazon 2 Microsoft 2
// https://leetcode.com/problems/array-partition/

// Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

// Example 1:
// Input: nums = [1,4,3,2]
// Output: 4
// Explanation: All possible pairings (ignoring the ordering of elements) are:
// 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
// 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
// 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
// So the maximum possible sum is 4.
// Example 2:
// Input: nums = [6,2,6,5,1,2]
// Output: 9
// Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.

class ArrayPartition {

  // brute force: O(nlogn) sort the input array and then the sum of 1st, 3rd, 5th..., is the answer.
  public int arrayPairSum(int[] nums) {
    Arrays.sort(nums);
    int sum = 0;
    for (int i = 0; i < nums.length; i += 2) {
      sum += nums[i];
    }
    return sum;
  }

  // counting sort O(n)
  // 1 <= n <= 10^4, negative can happen, so we need 10000*2+1 indexes
  public int arrayPairSum(int[] nums) {
    int[] count = new int[20001];
    for (int i = 0; i < nums.length; i++) {
      count[nums[i] + 10000]++; // handle negative
    }
    int sum = 0;
    boolean takeMinFromPair = true;
    for (int i = 0; i < count.length; i++) {
      while (count[i] > 0) {
        if (takeMinFromPair) {
          sum += i - 10000;
        }
        takeMinFromPair = !takeMinFromPair;
        count[i]--;
      }
    }
    return sum;
  }

  // counting sort O(n)
  // 1 <= n <= 10^4, negative can happen, so we need 10000*2+1 indexes
  public int arrayPairSum(int[] nums) {
    Map<Integer, Integer> numToCount = new HashMap<>();
    for (int num : nums) {
      numToCount.putIfAbsent(num, 0);
      numToCount.put(num, 1 + numToCount.get(num));
    }
    int sum = 0;
    boolean takeMinFromPair = true;
    for (int i = -10001; i < 10001; i++) {
      if (!numToCount.containsKey(i)) {
        continue;
      }
      while (numToCount.get(i) > 0) {
        if (takeMinFromPair) {
          System.out.println(i);
          sum += i;
        }
        takeMinFromPair = !takeMinFromPair;
        numToCount.put(i, numToCount.get(i) - 1);
      }
    }

    return sum;
  }
}
