// Array, Dynamic Programming, Greedy
// Amazon 10 Goldman Sachs 4 Bloomberg 3 Adobe 3 Apple 2 Google 2 Microsoft 2 Salesforce 2 DoorDash 2 PhonePe 2 ShareChat 4 Uber 2 Tesla 2 Snapchat 3 Facebook 3 Yahoo 3 Flipkart 3 TikTok 3 Morgan Stanley 2 Oracle 2 ByteDance 2 tcs 2 Citrix 2 Infosys 2 payu 2
// https://leetcode.com/problems/jump-game-ii/

// You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

// Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

// 0 <= j <= nums[i] and
// i + j < n
// Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

// Example 1:
// Input: nums = [2,3,1,1,4]
// Output: 2
// Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

// Example 2:
// Input: nums = [2,3,0,1,4]
// Output: 2

class JumpGameII {

  // brute force with memoization
  public int jump(int[] nums) {
    Map<Integer, Integer> indexToMinJump = new HashMap<>();
    return jumpHelperMemoized(nums, 0, indexToMinJump);
  }

  private int jumpHelperMemoized(
    int[] nums,
    int index,
    Map<Integer, Integer> indexToMinJump
  ) {
    if (index >= nums.length - 1) {
      return 0;
    }

    if (indexToMinJump.containsKey(index)) {
      return indexToMinJump.get(index);
    }

    int minSteps = nums.length;
    int maxJump = nums[index];
    for (int jump = 1; jump <= maxJump; jump++) {
      minSteps =
        Math.min(
          minSteps,
          1 + this.jumpHelperMemoized(nums, index + jump, indexToMinJump)
        );
    }

    indexToMinJump.put(index, minSteps);

    return minSteps;
  }

  // brute force try all the moves
  // O(2^n)
  public int jump(int[] nums) {
    return jumpHelper(nums, 0);
  }

  private int jumpHelper(int[] nums, int index) {
    if (index >= nums.length - 1) {
      return 0;
    }

    int minSteps = nums.length; // Integer.MAX_VALUE will overflow in stack calls, so use the max possible steps, the array length
    for (int jump = 1; jump <= nums[index]; jump++) {
      minSteps = Math.min(minSteps, 1 + this.jumpHelper(nums, index + jump));
    }

    return minSteps;
  }
}
