// Array, Two Pointers, Sorting
// Amazon 12 Apple 6 Microsoft 5 Yahoo 3 ServiceNow 3 Google 2 Bloomberg 2 VMware 2 Adobe 2 Uber 4 Facebook 4 Salesforce 3 Nvidia 3 Grab 3 Walmart Global Tech 2 Samsung 2 Intel 2 Oracle 2 eBay 2 Visa 2 Spotify 2 Swiggy 2 Tesla 2 Sprinklr 2 Pocket Gems
// https://leetcode.com/problems/sort-colors/description/
// Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

// We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

// You must solve this problem without using the library's sort function.

// Example 1:
// Input: nums = [2,0,2,1,1,0]
// Output: [0,0,1,1,2,2]
// Example 2:
// Input: nums = [2,0,1]
// Output: [0,1,2]
class SortColors {

  // easy solution would be two passes
  // pass1 moves all the 0s and pass2 moves all the 1s

  // three pointers to track the rightmost boundary of zeros, the leftmost boundary of twos and the current element under the consideration.
  // like a partition but for 3 parts
  public void sortColors(int[] nums) {
    int zero = 0; // index smaller than zero should only have 1 as the value
    int two = nums.length - 1; // index bigger than two should only have 2 as the value
    int current = 0;
    while (current <= two) {
      if (nums[current] == 0) {
        int rightmostZeroCopy = nums[zero];
        nums[zero] = nums[current];
        nums[current] = rightmostZeroCopy;
        zero++;
        current++;
      } else if (nums[current] == 2) {
        int leftostTwoCopy = nums[two];
        nums[two] = nums[current];
        nums[current] = leftostTwoCopy;
        two--;
      } else {
        // 1, noop
        current++;
      }
    }
  }
}
