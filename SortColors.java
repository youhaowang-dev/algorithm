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

  // brute force: counting sort

  // easy solution would be two passes
  // pass1 moves all the 0s and pass2 moves all the 1s

  // one pass: swap 0 to left and 2 to right, so 1 is in the middle
  // three pointers to track the tail of 0, the head of 2, and the current swap position
  public void sortColors(int[] nums) {
    int zerosTail = 0;
    int twosHead = nums.length - 1;
    int current = 0;
    while (current <= twosHead) {
      int currentVal = nums[current];
      // 0, move 0 to zero tail
      if (currentVal == 0) {
        int zeroTailCopy = nums[zerosTail];
        nums[zerosTail] = currentVal;
        nums[current] = zeroTailCopy;
        zerosTail++;
        current++;
        continue;
      }
      // 2, move 2 to two head, donot move current as the swapped value coult be 0
      if (currentVal == 2) {
        int twoHeadCopy = nums[twosHead];
        nums[twosHead] = currentVal;
        nums[current] = twoHeadCopy;
        twosHead--;
        continue;
      }

      // 1, noop, move current
      if (currentVal == 1) {
        current++;
      }
    }
  }
}
