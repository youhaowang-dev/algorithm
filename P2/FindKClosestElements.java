// Array, Two Pointers, Binary Search, Sliding Window, Sorting, Heap (Priority Queue)
// Amazon 8 Adobe 5 DoorDash 3 Google 2 Facebook 2 Bloomberg 2 Apple 2 TikTok 2 Uber 2 Oracle 2 Microsoft 13 Paypal 4 LinkedIn 2 Goldman Sachs 2 ByteDance 2
// https://leetcode.com/problems/find-k-closest-elements/description/

// Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

// An integer a is closer to x than an integer b if:

// |a - x| < |b - x|, or
// |a - x| == |b - x| and a < b

// Example 1:
// Input: arr = [1,2,3,4,5], k = 4, x = 3
// Output: [1,2,3,4]
// Example 2:
// Input: arr = [1,2,3,4,5], k = 4, x = -1
// Output: [1,2,3,4]

class FindKClosestElements {

  // search A[left] < target, A[right] >= target => expand left and right => build result
  // time: O(logn + 2k)
  public List<Integer> findClosestElements(int[] nums, int k, int target) {
    // get the two neighbors that are closest to target
    // A[left] < target, A[right] >= target
    int right = this.findUpperClosest(nums, target);
    int left = right - 1;

    for (int i = 0; i < k; i++) {
      if (this.isLeftCloser(nums, target, left, right)) {
        left--;
      } else {
        right++;
      }
    }
    // left could be -1 and right could be length

    List<Integer> result = new ArrayList<>();
    for (int i = left + 1; i < right; i++) {
      result.add(nums[i]);
    }

    return result;
  }

  private int findUpperClosest(int[] nums, int target) {
    int left = 0;
    int right = nums.length - 1;
    while (left + 1 < right) {
      int mid = left + (right - left) / 2;
      if (nums[mid] >= target) {
        right = mid;
      } else {
        left = mid;
      }
    }

    if (nums[left] >= target) {
      return left;
    }

    if (nums[right] >= target) {
      return right;
    }

    return nums.length; // not found
  }

  private boolean isLeftCloser(int[] nums, int target, int left, int right) {
    if (left < 0) {
      return false;
    }
    if (right >= nums.length) {
      return true;
    }
    return (target - nums[left]) <= (nums[right] - target);
  }

  // sort and slice and sort again
  // time O(N⋅log(N)+k⋅log(k))
  // space O(N)
  public List<Integer> findClosestElements(int[] arr, int k, int target) {
    List<Integer> nums = this.getNumList(arr);
    // sort distance ASC; do not use Arrays.sort as it only works for int not Integer
    Collections.sort(
      nums,
      (a, b) -> Math.abs(target - a) - Math.abs(target - b)
    );

    List<Integer> result = nums.subList(0, k);
    Collections.sort(result);

    return result;
    // return IntStream
    //   .of(arr)
    //   .boxed()
    //   .sorted(Comparator.comparingInt(a -> Math.abs(a - x)))
    //   .limit(k)
    //   .sorted()
    //   .collect(Collectors.toList());
  }

  private List<Integer> getNumList(int[] arr) {
    List<Integer> nums = new ArrayList<>();
    for (int num : arr) {
      nums.add(num);
    }

    return nums;
  }

  // two pointers O(n)
  public List<Integer> findClosestElements(int[] arr, int k, int x) {
    int left = 0;
    int right = arr.length - 1;
    while (right - left >= k) {
      if (Math.abs(arr[left] - x) > Math.abs(arr[right] - x)) {
        left++;
      } else {
        right--;
      }
    }
    List<Integer> result = new ArrayList<>(k);
    for (int i = left; i <= right; i++) {
      result.add(arr[i]);
    }
    return result;
  }

  // binary search time O(log(N−k)+k) space O(1)
  // right is bounded by length - k, so left=0 and right=len-k
  // compare (target - nums[mid]) and (nums[mid+k] - target)
  // At the end of the binary search, we have located the leftmost index for the final answer.
  public List<Integer> findClosestElements(int[] nums, int k, int target) {
    int left = 0;
    int right = nums.length - k;

    while (left < right) {
      int mid = (left + right) / 2;
      if (target - nums[mid] > nums[mid + k] - target) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }

    List<Integer> result = new ArrayList<>();
    for (int i = left; i < left + k; i++) {
      result.add(nums[i]);
    }

    return result;
  }
}
