// Array, Two Pointers, Sorting
// Amazon 8 Adobe 6 Apple 4 Facebook 4 Bloomberg 3 Uber 2 Google 2 Microsoft 3 Goldman Sachs 2 TikTok 2 Capital One 7 Oracle 3 Cisco 2 Rubrik 2 Qualtrics 2
// https://leetcode.com/problems/3sum-closest/

// Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

// Return the sum of the three integers.

// You may assume that each input would have exactly one solution.

// Example 1:
// Input: nums = [-1,2,1,-4], target = 1
// Output: 2
// Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
// Example 2:
// Input: nums = [0,0,0], target = 1
// Output: 0
// Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
class ThreeSumClosest {

  // three pointers
  // If an interviewer asks you whether you can achieve O(1) memory complexity,
  // you can use the selection sort instead of a built-in sort in the Two Pointers approach.
  // It will make it a bit slower, though the overall time complexity will be still O(n^2)
  public int threeSumClosest(int[] nums, int target) {
    Arrays.sort(nums);
    int closestSum = Integer.MAX_VALUE;
    for (int i = 0; i < nums.length; i++) {
      // optional
      // if (i > 0 && nums[i] == nums[i - 1]) {
      //   continue;
      // }
      int left = i + 1;
      int right = nums.length - 1;
      while (left < right) {
        int currentSum = nums[i] + nums[left] + nums[right];
        if (currentSum == target) {
          return currentSum;
        }

        // update closestSum
        if (Math.abs(currentSum - target) < Math.abs(closestSum - target)) {
          closestSum = currentSum;
        }

        // update pointers
        if (currentSum < target) {
          left++;
          // optional
          // while (left < nums.length && nums[left] == nums[left - 1]) {
          //   left++;
          // }
        } else {
          right--;
          // optional
          // while (right >= 0 && nums[right] == nums[right + 1]) {
          //   right--;
          // }
        }
      }
    }

    return closestSum;
  }
}
