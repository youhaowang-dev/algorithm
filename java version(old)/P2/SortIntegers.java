// https://www.lintcode.com/problem/463/
// Given an integer array, sort it in ascending order. Use selection sort, bubble sort, insertion sort or any O(n2) algorithm.
class SortIntegers {

  public void sortIntegers(int[] nums) {
    this.selectionSort(nums);
  }

  // selection sort: select min in each loop, swap it to head
  private void selectionSort(int[] nums) {
    for (int i = 0; i < nums.length; i++) {
      int minIndex = this.getMinIndex(nums, i);
      this.swap(nums, minIndex, i);
    }
  }

  private int getMinIndex(int[] nums, int start) {
    int minIndex = start;
    int min = nums[start];
    for (int i = start; i < nums.length; i++) {
      if (min > nums[i]) {
        minIndex = i;
        min = nums[i];
      }
    }

    return minIndex;
  }

  // bubble sort: repeatedly swapping the adjacent elements if they are in the wrong order
  public void bubbleSort(int[] nums) {
    int n = nums.length;
    for (int i = 0; i < n - 1; i++) {
      boolean sorted = true; // optional
      for (int j = 0; j < n - i - 1; j++) {
        if (nums[j] > nums[j + 1]) {
          this.swap(nums, j, j + 1);
          sorted = false;
        }
      }
      if (sorted) {
        break;
      }
    }
  }

  private void swap(int[] nums, int a, int b) {
    int numACopy = nums[a];
    nums[a] = nums[b];
    nums[b] = numACopy;
  }

  private void insertionSort(int nums[]) {
    for (int i = 1; i < nums.length; ++i) {
      int current = nums[i];
      int j = i - 1;

      // Move elements of nums[0..i-1], that are greater than current, to one position ahead of their current position
      while (j >= 0 && nums[j] > current) {
        nums[j + 1] = nums[j];
        j = j - 1;
      }
      nums[j + 1] = current;
    }
  }
}
