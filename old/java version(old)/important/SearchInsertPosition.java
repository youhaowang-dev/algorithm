// Array, Binary Search
// Apple 9 Google 4 Amazon 4 Microsoft 4 Adobe 3 Yahoo 2
// source: https://leetcode.com/problems/search-insert-position/description/
// description: Given a sorted array of distinct integers and a target value,
//              return the index if the target is found. If not, return the index where it would be if it were inserted in order.
//              You must write an algorithm with O(log n) runtime complexity.
// example: Input: nums = [1,3,5,6], target = 5, Output: 2
//          Input: nums = [1,3,5,6], target = 2, Output: 1
//          Input: nums = [1,3,5,6], target = 7, Output: 4

final class SearchInsertPosition {

  // find the biggest number smaller than target, return its position+1
  public int searchInsert(int[] nums, int target) {
    if (nums.length == 0) {
      return 0;
    }

    int left = 0;
    int right = nums.length - 1;
    while (left + 1 < right) {
      int mid = left - (left - right) / 2;
      int midNum = nums[mid];
      if (midNum == target) {
        return mid;
      }
      if (midNum > target) {
        right = mid;
      }
      if (midNum < target) {
        left = mid;
      }
    }

    // exit conditions: left == right or left + 1 == right
    // [1] => left == right
    // [1,2] => left == right
    // [1,2,3] => 0,2 => 0,1 or 1,0 => left + 1 == right

    // handle equals first
    int leftNum = nums[left];
    int rightNum = nums[right];
    if (leftNum == target) {
      return left;
    }
    if (rightNum == target) {
      return right;
    }

    // [start,left][left, end]
    if (left == right) {
      if (leftNum > target) {
        return left;
      }
      if (leftNum < target) {
        return left + 1;
      }
    }

    // [start,left][right, end]
    if (left + 1 == right) {
      // check left first as we want smaller position if possible; left is smaller
      if (leftNum > target) {
        return left;
      }
      if (leftNum < target && target < rightNum) {
        return right;
      }
      if (target > rightNum) {
        return right + 1;
      }
    }

    return -1; // should not reach this line; throw?
  }

  public static void main(String[] args) throws Exception {
    SearchInsertPosition SearchInsertPosition = new SearchInsertPosition();
    int[] nums = new int[] { 1, 3, 5, 6 };
    int[] testCases = new int[] { 2, 5, 7 };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] { "searchInsert" };

    for (int target : testCases) {
      for (String methodName : testMethodNames) {
        java.lang.reflect.Method method = SearchInsertPosition
          .getClass()
          .getMethod(methodName, int[].class, int.class);
        int insertIndex = (int) method.invoke(
          SearchInsertPosition,
          nums,
          target
        );

        System.out.println(
          String.format(
            "Method Name: %s\nInput: %s, Output: %s",
            methodName,
            java.util.Arrays.toString(nums) + " target: " + target,
            insertIndex
          )
        );
      }
    }
  }
}
