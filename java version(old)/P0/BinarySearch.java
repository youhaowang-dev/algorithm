// Array, Binary Search
// Apple 10 Google 6 Adobe 5 Amazon 4 Uber 4 Facebook 2 Microsoft 8 Bloomberg 4 Yahoo 3 tcs 2 SAP 4 Yandex 2 Oracle 2 Samsung 2 Goldman Sachs 2 Infosys 2
// https://leetcode.com/problems/binary-search/
// Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

// You must write an algorithm with O(log n) runtime complexity.

// Example 1:
// Input: nums = [-1,0,3,5,9,12], target = 9
// Output: 4
// Explanation: 9 exists in nums and its index is 4
// Example 2:
// Input: nums = [-1,0,3,5,9,12], target = 2
// Output: -1
// Explanation: 2 does not exist in nums so return -1

class BinarySearch {

  public int search(int[] nums, int target) {
    int left = 0;
    int right = nums.length - 1;
    // + 1 never infinite loop
    while (left + 1 < right) {
      int mid = left + (right - left) / 2;
      int midVal = nums[mid];
      if (midVal == target) {
        return mid;
      }
      if (midVal > target) {
        right = mid;
      }
      if (midVal < target) {
        left = mid;
      }
    }
    // handled terminated cases
    if (nums[left] == target) {
      return left;
    }
    if (nums[right] == target) {
      return right;
    }

    return -1;
  }
}
