// Array, Prefix Sum
// Amazon 16 Apple 6 Bloomberg 6 Microsoft 4 Adobe 4 Facebook 3 Walmart Global Tech 3 American Express 3 Google 2 Uber 2 Salesforce 2 DE Shaw 2 Asana 14 Lyft 3 Yahoo 3 Oracle 3 Groupon 2 Qualtrics 2 TikTok 2 IBM 2 Paypal 5 Goldman Sachs 5 Intel 4 Expedia 3 VMware 3 Nutanix 2 Nvidia 2 ServiceNow 2 Indeed 2 Arista Networks 2 PayTM 2 MakeMyTrip 2 Zillow 2 LinkedIn

// Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

// You must write an algorithm that runs in O(n) time and without using the division operation.

// Example 1:
// Input: nums = [1,2,3,4]
// Output: [24,12,8,6]
// Example 2:
// Input: nums = [-1,1,0,-3,3]
// Output: [0,0,9,0,0]

// Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

class ProductOfArrayExceptSelf {

  // preprocess data from both ends
  // multiply from left and multiply from right
  // so for an index we can easily find the left and right products
  public int[] productExceptSelf(int[] nums) {
    // build left products
    int[] leftProducts = new int[nums.length];
    leftProducts[0] = nums[0];
    for (int i = 1; i < nums.length; i++) {
      leftProducts[i] = nums[i] * leftProducts[i - 1];
    }

    // build right products
    int[] rightProducts = new int[nums.length];
    rightProducts[nums.length - 1] = nums[nums.length - 1];
    for (int i = nums.length - 2; i > 0; i--) {
      rightProducts[i] = nums[i] * rightProducts[i + 1];
    }

    // build result
    int[] result = new int[nums.length];
    result[0] = rightProducts[1];
    result[nums.length - 1] = leftProducts[nums.length - 1 - 1];
    for (int i = 1; i < nums.length - 1; i++) {
      int leftProduct = leftProducts[i - 1];
      int rightProduct = rightProducts[i + 1];
      result[i] = leftProduct * rightProduct;
    }

    return result;
  }

  // space optimized
  // keep track of leftProduct and rightProduct
  // two passes to build the result
  public int[] productExceptSelf(int[] nums) {
    int[] result = new int[nums.length];
    result[0] = nums[0];
    result[nums.length - 1] = nums[nums.length - 1];

    int leftProduct = 1;
    for (int i = 0; i < nums.length; i++) {
      result[i] = leftProduct;
      leftProduct = leftProduct * nums[i];
    }

    int rightProduct = 1;
    for (int i = nums.length - 1; i >= 0; i--) {
      result[i] = result[i] * rightProduct;
      rightProduct = rightProduct * nums[i];
    }

    return result;
  }
}
