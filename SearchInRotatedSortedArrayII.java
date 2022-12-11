// Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
final class SearchInRotatedSortedArrayII {
  // with duplicates, we cannot tell the partition the target belongs to.
  // so the pointer can only move forward by 1 and the worst complexity can be O(n)
  // [1,1,1,1,1,1,] target=2
}
