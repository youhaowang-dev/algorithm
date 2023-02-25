// Array, Two Pointers, Sorting
// Amazon 11 Apple 4 Bloomberg 4 Facebook 3 Audible 2 Google 4 Adobe 3 Uber 3 Microsoft 3 Infosys 3 LinkedIn 2 Rubrik 2 Yahoo 4 Snapchat 4

// Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

// 0 <= a, b, c, d < n
// a, b, c, and d are distinct.
// nums[a] + nums[b] + nums[c] + nums[d] == target
// You may return the answer in any order.

// Example 1:
// Input: nums = [1,0,-1,0,-2,2], target = 0
// Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
// Example 2:
// Input: nums = [2,2,2,2,2], target = 8
// Output: [[2,2,2,2]]

class FourSum {

  // depth first search
  // can easily convert to kth for followup
  // use long for sum if interviewer say numbers are large and can overflow
  public List<List<Integer>> fourSum(int[] nums, int target) {
    List<List<Integer>> results = new ArrayList<>();
    Arrays.sort(nums);
    this.searchSum(nums, new ArrayList<Integer>(), target, results, 0);
    return results;
  }

  private void searchSum(
    int[] nums,
    ArrayList<Integer> list,
    int target,
    List<List<Integer>> results,
    int start
  ) {
    if (list.size() == 4) {
      if (target == 0) {
        results.add(new ArrayList<Integer>(list));
      }
      return;
    }
    for (int i = start; i < nums.length; i++) {
      if (i != start && nums[i] == nums[i - 1]) {
        continue;
      }
      list.add(nums[i]);
      this.searchSum(nums, list, target - nums[i], results, i + 1);
      list.remove(list.size() - 1);
    }
  }

  public List<List<Integer>> fourSum(int[] nums, int target) {
    List<List<Integer>> results = new ArrayList<>();
    Arrays.sort(nums);
    int k = 4;
    this.searchKSum(nums, new ArrayList<Integer>(), target, results, 0, k);
    return results;
  }

  private void searchKSum(
    int[] nums,
    ArrayList<Integer> list,
    int target,
    List<List<Integer>> results,
    int start,
    int k
  ) {
    if (list.size() == k) {
      if (target == 0) {
        results.add(new ArrayList<Integer>(list));
      }
      return;
    }
    for (int i = start; i < nums.length; i++) {
      if (i != start && nums[i] == nums[i - 1]) {
        continue;
      }
      list.add(nums[i]);
      this.searchKSum(nums, list, target - nums[i], results, i + 1, k);
      list.remove(list.size() - 1);
    }
  }

  // four pointers
  public List<List<Integer>> fourSum(int[] nums, int target) {
    Set<List<Integer>> results = new HashSet<List<Integer>>();
    Arrays.sort(nums);
    int size = nums.length;
    List<List<Integer>> ans = new ArrayList<>();
    for (int i = 0; i < size - 3; i++) {
      for (int j = i + 1; j < size - 2; j++) {
        if (j > i + 1 && nums[j] == nums[j - 1]) {
          continue;
        }
        int left = j + 1;
        int right = size - 1;
        while (left < right) {
          int sum = nums[i] + nums[j] + nums[left] + nums[right];
          if (sum == target) {
            List<Integer> result = new ArrayList<>();
            result.add(nums[i]);
            result.add(nums[j]);
            result.add(nums[left]);
            result.add(nums[right]);
            results.add(result);
            left++;
            right--;
          } else if (sum < target) {
            left++;
          } else {
            right--;
          }
        }
      }
    }

    return new ArrayList<List<Integer>>(results);
  }
}
