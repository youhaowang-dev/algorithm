// Array, Binary Search, Divide and Conquer
// Amazon 21 Bloomberg 10 Microsoft 7 Apple 7 Adobe 5 Media.net 5 Facebook 4 LinkedIn 4 Uber 3 Yahoo 2 Google 2 TikTok 2
// https://leetcode.com/problems/search-in-rotated-sorted-array/
//              There is an integer array nums sorted in ascrighting order (with distinct values).
//              Prior to being passed to your function, nums is possibly rotated at an unknown pivot
//              index k (1 <= k < nums.length) such that the resulting array is
//              [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
//              For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
//              Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
//              You must write an algorithm with O(log n) runtime complexity.
// Example 1:
// Input: nums = [4,5,6,7,0,1,2], target = 0
// Output: 4

// Example 2:
// Input: nums = [4,5,6,7,0,1,2], target = 3
// Output: -1

// Example 3:
// Input: nums = [1], target = 0
// Output: -1

final class SearchInRotatedSortedArray {

  // brute force: linear scan O(n)

  // TODO: use class SearchState {left, right, getMid, leftIsSorted, rightIsSorted, searchLeftNext, searchRightNext}

  // binary search O(logn)
  // 4,5,6,7,0,1,2
  // l t   m     r => left sorted and t in left       => r move to m
  // l     m   t r => left sorted but t not in left   => l move to m
  // 4,5,6,7,0,1,2
  //   l t   m   r => right sorted but t not in right => r move to m
  //   l     m t r => right sorted and t in right     => l move to m
  // mid can split the rotated array in two parts; one part is sorted, the other part is unsorted
  // handle the sorted part by additionaly checking if the target in this part
  // if sorted part contains the target, continue search in this part
  // if sorted part does not contain the target, continue search the other part
  public int search(int[] nums, int target) {
    if (nums == null || nums.length == 0) {
      return -1;
    }
    int left = 0;
    int right = nums.length - 1;
    while (left + 1 < right) {
      int mid = left - (left - right) / 2;
      int midVal = nums[mid];
      int leftVal = nums[left];
      int rightVal = nums[right];
      // handle equals
      if (midVal == target) {
        return mid;
      }
      if (leftVal == target) {
        return left;
      }
      if (rightVal == target) {
        return right;
      }
      // left is sorted
      boolean leftPartSorted = leftVal < midVal;
      boolean targetInLeftPart = leftVal < target && target < midVal;
      if (leftPartSorted) {
        if (targetInLeftPart) {
          right = mid;
        } else {
          left = mid;
        }
      }
      // right is sorted
      boolean rightPartSorted = midVal < rightVal;
      boolean targetInRightPart = midVal < target && target < rightVal;
      if (rightPartSorted) {
        if (targetInRightPart) {
          left = mid;
        } else {
          right = mid;
        }
      }
    }

    if (nums[left] == target) {
      return left;
    }

    if (nums[right] == target) {
      return right;
    }

    return -1;
  }

  public int search(int[] nums, int target) {
    if (nums.length == 0) {
      return -1;
    }

    BinarySearchTarget search = new BinarySearchTarget(nums, target);
    while (search.unfinished()) {
      Integer searchTarget = search.targetFound();
      if (searchTarget != null) {
        return (int) searchTarget;
      }
      search.updateLeftPart();
      search.updateRightPart();
    }

    if (search.getLeftVal() == target) {
      return search.left;
    }

    if (search.getRightVal() == target) {
      return search.right;
    }

    return -1;
  }

  private class BinarySearchTarget {

    public int left; // TODO: make private
    public int right; // TODO: make private
    private int target;
    private int[] nums;

    public BinarySearchTarget(int[] nums, int target) {
      this.left = 0;
      this.right = nums.length - 1;
      this.target = target;
      this.nums = nums;
    }

    public boolean unfinished() {
      return this.left + 1 < this.right;
    }

    public Integer targetFound() {
      if (this.getMidVal() == this.target) {
        return this.getMid();
      }
      if (this.getLeftVal() == this.target) {
        return this.left;
      }
      if (this.getRightVal() == this.target) {
        return this.right;
      }

      return null;
    }

    public void updateLeftPart() {
      if (this.leftPartSorted()) {
        if (this.targetInLeftPart()) {
          this.right = this.getMid();
        } else {
          this.left = this.getMid();
        }
      }
    }

    public void updateRightPart() {
      if (this.rightPartSorted()) {
        if (this.targetInRightPart()) {
          this.left = this.getMid();
        } else {
          this.right = this.getMid();
        }
      }
    }

    private int getLeftVal() {
      return this.nums[this.left];
    }

    private int getRightVal() {
      return this.nums[this.right];
    }

    private int getMidVal() {
      return this.nums[this.getMid()];
    }

    private int getMid() {
      return this.left + (this.right - this.left) / 2;
    }

    private boolean leftPartSorted() {
      return this.getLeftVal() < this.getMidVal();
    }

    private boolean targetInLeftPart() {
      return this.getLeftVal() < this.target && this.target < this.getMidVal();
    }

    private boolean rightPartSorted() {
      return this.getMidVal() < this.getRightVal();
    }

    private boolean targetInRightPart() {
      return this.getMidVal() < this.target && this.target < this.getRightVal();
    }
  }

  // 1. binary search the min index
  // 2. binary search the target in the sorted part
  public int search(int[] nums, int target) {
    if (nums.length == 0) {
      return -1;
    }

    int minIndex = this.findMinIndex(nums);
    // if min is -1, that means the array is not rotated, the following code still works
    int rightVal = nums[nums.length - 1];
    if (target == rightVal) {
      return nums.length - 1;
    }

    boolean targetInLeftPart = target > rightVal;
    int left = targetInLeftPart ? 0 : minIndex;
    int right = targetInLeftPart ? minIndex - 1 : nums.length - 1;
    while (left + 1 < right) {
      int mid = left - (left - right) / 2;
      int midVal = nums[mid];
      if (midVal == target) {
        return mid;
      }
      if (midVal < target) {
        left = mid;
      }
      if (midVal > target) {
        right = mid;
      }
    }

    // if not found, index could go out of bound
    if (left >= 0 && left <= nums.length - 1 && nums[left] == target) {
      return left;
    }
    if (right >= 0 && right <= nums.length - 1 && nums[right] == target) {
      return right;
    }

    return -1;
  }

  private int findMinIndex(int[] nums) {
    int left = 0;
    int right = nums.length - 1;
    while (left + 1 < right) {
      int mid = left - (left - right) / 2;
      int midVal = nums[mid];
      int rightVal = nums[right];
      if (midVal < rightVal) {
        right = mid;
      }
      if (midVal > rightVal) {
        left = mid;
      }
      // == let /2 happen
    }

    if (nums[left] < nums[right]) {
      return left;
    }

    if (nums[left] > nums[right]) {
      return right;
    }

    return -1;
  }
}
