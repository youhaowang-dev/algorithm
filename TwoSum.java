class TwoSum {

  // O(n) space and time
  public int[] twoSum(int[] nums, int target) {
    HashMap<Integer, Integer> numToIndex = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
      int num = nums[i];
      int otherNum = target - num;
      if (numToIndex.containsKey(otherNum)) {
        return new int[] { i, numToIndex.get(otherNum) };
      } else {
        numToIndex.put(num, i);
      }
    }

    return new int[] { 0, 0 };
  }

  // brute force
  // O(n^2) time
  // O(1) space
  public int[] twoSum(int[] nums, int target) {
    // i and j are indexes of nums
    for (int i = 0; i < nums.length; i++) {
      for (int j = i + 1; j < nums.length; j++) {
        if (nums[i] + nums[j] == target) {
          return new int[] { i, j };
        }
      }
    }

    return new int[] { 0, 0 };
  }
}
