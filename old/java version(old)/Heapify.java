// https://www.lintcode.com/problem/130/description
// Given an integer array, heapify it into a min-heap array.

// For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].
class Heapify {

  /*
   * @param A: Given an integer array
   * @return: nothing
   */
  public void heapify(int[] A) {
    // we don't need to sift down the leaf nodes since they trivially satisfy
    // the heap property already. Only need to start from the second last level
    // for (int i = (A.length - 1) / 2; i >= 0; i--) {
    for (int i = A.length - 1; i >= 0; i--) {
      this.siftDown(A, i);
    }
  }

  private void siftDown(int[] nums, int idx) {
    int child;
    while (2 * idx + 1 < nums.length) {
      child = 2 * idx + 1; // set child to be the left child

      // compare the left child with the right child to find the minimum one
      if (child + 1 < nums.length && nums[child + 1] < nums[child]) {
        child += 1;
      }

      if (nums[idx] <= nums[child]) {
        return;
      }

      // swap their values
      int temp = nums[idx];
      nums[idx] = nums[child];
      nums[child] = temp;

      // continue to sift down
      idx = child;
    }
  }
}
