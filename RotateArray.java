// Array, Math, Two Pointers
// Amazon 10 Apple 7 Microsoft 3 Yahoo 3 Adobe 2 Facebook 2
// Given an array, rotate the array to the right by k steps, where k is non-negative.

// Example 1:
// Input: nums = [1,2,3,4,5,6,7], k = 3
// Output: [5,6,7,1,2,3,4]
// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]
// rotate 2 steps to the right: [6,7,1,2,3,4,5]
// rotate 3 steps to the right: [5,6,7,1,2,3,4]

// Example 2:
// Input: nums = [-1,-100,3,99], k = 2
// Output: [3,99,-1,-100]
// Explanation:
// rotate 1 steps to the right: [99,-1,-100,3]
// rotate 2 steps to the right: [3,99,-1,-100]
import java.util.*;

final class RotateArray {

  // Option 1: The simplest approach is to rotate all the elements of the
  // array in kkk steps by rotating the elements by 1 unit in each step.
  // Option 2: We use an extra array in which we place every element of the
  // array at its correct position i.e. the number at index iii in the original array is placed at the index (i+k)% length of array. Then, we copy the new array to the original one.

  // Option 3: inplace solution, 3 reverses
  // Let n=7 and k=3.
  // Original List                   : 1 2 3 4 5 6 7
  // After reversing all numbers     : 7 6 5 4 3 2 1
  // After reversing first k numbers : 5 6 7 4 3 2 1
  // After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
  public void rotate(int[] nums, int k) {
    k = k % nums.length; // optimization & handle cases like [1]
    // rotate 3 times => last 3 move to front => partition [0, length - 1 - 3],[length - 1 - (3 - 1) ,length - 1]
    this.reverse(nums, nums.length - 1 - (k - 1), nums.length - 1); // rotate the numbers moving to front
    this.reverse(nums, 0, nums.length - 1 - k); // rotate the rest
    this.reverse(nums, 0, nums.length - 1); // rotate all to revert back to the original order
  }

  private void reverse(int[] nums, int start, int end) {
    while (start < end) {
      int startCopy = nums[start];
      nums[start] = nums[end];
      nums[end] = startCopy;
      start++;
      end--;
    }
  }

  public static void main(String[] args) throws Exception {
    RotateArray RotateArray = new RotateArray();
    int[] array = new int[] { 1, 2, 3, 4, 5, 6, 7 };
    int[] rotates = new int[] { 0, 1, 2, 3, 700 };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] { "rotate" };

    for (int rotate : rotates) {
      for (String methodName : testMethodNames) {
        int[] arrayCopy = Arrays.copyOfRange(array, 0, array.length);
        System.out.println("methodName: " + methodName);
        System.out.println("arrayCopy: " + Arrays.toString(arrayCopy));
        System.out.println("rotate: " + rotate);
        java.lang.reflect.Method method = RotateArray
          .getClass()
          .getMethod(methodName, int[].class, int.class);
        method.invoke(RotateArray, arrayCopy, rotate);

        System.out.println("arrayCopy: " + Arrays.toString(arrayCopy));
        System.out.println();
      }
    }
  }
}
