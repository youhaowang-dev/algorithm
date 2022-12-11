// Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set
// Google 5 Apple 3 Amazon 3 Microsoft 3 Adobe 2 Bloomberg 2 Infosys 2 Uber 4 Myntra 3 Walmart Global Tech 2 Sprinklr 2
// https://leetcode.com/problems/count-of-smaller-numbers-after-self/

// Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

// Example 1:
// Input: nums = [5,2,6,1]
// Output: [2,1,1,0]
// Explanation:
// To the right of 5 there are 2 smaller elements (2 and 1).
// To the right of 2 there is only 1 smaller element (1).
// To the right of 6 there is 1 smaller element (1).
// To the right of 1 there is 0 smaller element.

// Example 2:
// Input: nums = [-1]
// Output: [0]

// Example 3:
// Input: nums = [-1,-1]
// Output: [0,0]
import java.util.*;

final class CountOfSmallerNumbersAfterSelf {

  public List<Integer> countSmallerQuickSort(int[] nums) {
    int[] numsSorted = nums.clone();
    this.quickSort(numsSorted, 0, nums.length - 1);
    Map<Integer, Integer> numberToCount = new HashMap<>();
    for (int index = 0; index < numsSorted.length; index++) {
      // [1,2,3]
      // 1 expect 2, so 3(length) - 0(index) - 1
      // 2 expect 1, so 3(length) - 1(index) - 1
      int count = numsSorted.length - index - 1;
      numberToCount.put(numsSorted[index], count);
    }
    List<Integer> counts = new ArrayList<>();
    for (int num : nums) {
      counts.add(numberToCount.get(num));
    }

    return counts;
  }

  private void quickSort(int[] nums, int first, int last) {
    if (first >= last) {
      return;
    }
    int partitionIndex = this.partition(nums, first, last);
    this.quickSort(nums, first, partitionIndex - 1);
    this.quickSort(nums, partitionIndex, last);
  }

  private int partition(int[] nums, int first, int last) {
    int partitionIndex = 0;
    int pivotValue = nums[last];
    for (int index = 0; index < last; index++) {
      if (nums[index] <= pivotValue) {
        this.swap(nums, index, partitionIndex);
        partitionIndex++;
      }
    }
    swap(nums, partitionIndex, last);

    return partitionIndex;
  }

  private void swap(int[] nums, int index1, int index2) {
    int index1Copy = nums[index1];
    nums[index1] = nums[index2];
    nums[index2] = index1Copy;
  }

  public static void main(String[] args) throws Exception {
    CountOfSmallerNumbersAfterSelf CountOfSmallerNumbersAfterSelf = new CountOfSmallerNumbersAfterSelf();
    int[][] testCases = new int[][] { { 5, 2, 6, 1 }, { -1 }, { -1, -1 } };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] { "countSmallerQuickSort" };

    for (int[] nums : testCases) {
      for (String methodName : testMethodNames) {
        java.lang.reflect.Method method = CountOfSmallerNumbersAfterSelf
          .getClass()
          .getMethod(methodName, int[].class);
        ArrayList<Integer> counts = (ArrayList<Integer>) method.invoke(
          CountOfSmallerNumbersAfterSelf,
          nums
        );

        System.out.println("methodName: " + methodName);
        System.out.println("nums: " + Arrays.toString(nums));
        System.out.println("counts: " + Arrays.toString(counts.toArray()));
      }
    }
  }
}
