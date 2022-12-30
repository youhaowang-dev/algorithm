// https://wentao-shao.gitbook.io/leetcode/binary-search/search-in-a-big-sorted-array
// Given a big sorted array with positive integers sorted by ascending order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++). Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.
// Return -1, if the number doesn't exist in the array.
class SearchinaBigSortedArray {

  public int searchBigSortedArray(ArrayReader reader, int target) {
    int leftIndex = 0;
    while (reader.get(leftIndex) < target) {
      leftIndex *= 2;
    }
    int left = leftIndex / 2;
    int right = leftIndex;

    while (left + 1 < right) {
      int mid = left + (right - left) / 2;
      int midVal = reader.get(mid);
      if (midVal == target) {
        right = mid;
      }
      if (midVal > target) {
        right = mid;
      }
      if (midVal < target) {
        left = mid;
      }
    }
    if (reader.get(left) == target) {
      return left;
    }
    if (reader.get(right) == target) {
      return right;
    }

    return -1;
  }
}
