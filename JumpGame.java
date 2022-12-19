// Array, Dynamic Programming, Greedy
// Amazon 20 Apple 5 Microsoft 5 Adobe 4 Google 4 Facebook 2 Bloomberg 2 Walmart Global Tech 2 Oracle 3 Salesforce 2 DoorDash 2 ByteDance 2 Flipkart 2 Docusign 2 Uber 4 Qualtrics 3 Goldman Sachs 3 TikTok 3 Paypal 2 Nutanix 2 Infosys 2 ShareChat 2
// https://leetcode.com/problems/jump-game/
// You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

// Return true if you can reach the last index, or false otherwise.

// Example 1:
// Input: nums = [2,3,1,1,4]
// Output: true
// Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

// Example 2:
// Input: nums = [3,2,1,0,4]
// Output: false
// Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

class JumpGame {

  // brute force
  // Time complexity : O(2^n). There are 2^n (upper bound) ways of jumping from the first position to the last, where nnn is the length of array nums
  public boolean canJump(int[] nums) {
    return this.canJumpFrom(nums, 0);
  }

  private boolean canJumpFrom(int[] nums, int index) {
    if (index == nums.length - 1) {
      return true;
    }

    int nextIndexMax = Math.min(index + nums[index], nums.length - 1);
    for (int nextIndex = index + 1; nextIndex < nextIndexMax + 1; nextIndex++) {
      if (this.canJumpFrom(nums, nextIndex)) {
        return true;
      }
    }

    return false;
  }
}
