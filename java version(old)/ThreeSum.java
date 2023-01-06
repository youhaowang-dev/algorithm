// Array, Two Pointers, Sorting
// Amazon 26 Apple 12 Facebook 8 Adobe 8 Microsoft 7 Bloomberg 6 Uber 4 Walmart Global Tech 4 Yahoo 3 MakeMyTrip 3 Goldman Sachs 2 Google 2 Visa 2 Cisco 2 TikTok 6 Salesforce 4 Infosys 4 Qualtrics 3 VMware 3 Morgan Stanley 3 LinkedIn 2 ByteDance 2 Oracle 2 Tesla 2 American Express 2 Intel 2
// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
// Notice that the solution set must not contain duplicate triplets.
//
// Example 1:
// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Explanation:
// nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
// nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
// nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
// The distinct triplets are [-1,0,1] and [-1,-1,2].
// Notice that the order of the output and the order of the triplets does not matter.
// Example 2:
// Input: nums = [0,1,1]
// Output: []
// Explanation: The only possible triplet does not sum up to 0.
// Example 3:
// Input: nums = [0,0,0]
// Output: [[0,0,0]]
// Explanation: The only possible triplet sums up to 0.

class ThreeSum {

  // modify input
  public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    List<List<Integer>> result = new ArrayList<>();
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] > 0) {
        break; // impossible for 0 sum
      }

      // allow init and skip dups
      if (i == 0 || nums[i - 1] != nums[i]) {
        this.twoSum(nums, i, result);
      }
    }

    return result;
  }

  // i is start index of nums
  private void twoSum(int[] nums, int i, List<List<Integer>> result) {
    Set<Integer> seen = new HashSet<>();
    for (int j = i + 1; j < nums.length; j++) {
      int sum = nums[i] + nums[j];
      int target = 0 - sum;
      if (seen.contains(target)) {
        result.add(Arrays.asList(nums[i], nums[j], target));
        // skip dups
        while (j + 1 < nums.length && nums[j] == nums[j + 1]) {
          j++;
        }
      }

      seen.add(nums[j]);
    }
  }

  // no sort
  public List<List<Integer>> threeSum(int[] nums) {
    Set<List<Integer>> res = new HashSet<>();
    Set<Integer> firstNums = new HashSet<>();
    Map<Integer, Integer> seen = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
      // add() return true if not in set
      if (firstNums.add(nums[i])) {
        for (int j = i + 1; j < nums.length; j++) {
          int sum = nums[i] + nums[j];
          int target = 0 - sum;
          if (seen.containsKey(target) && seen.get(target) == i) {
            List<Integer> triplet = Arrays.asList(nums[i], nums[j], target);
            Collections.sort(triplet);
            res.add(triplet);
          }
          seen.put(nums[j], i);
        }
      }
    }
    return new ArrayList(res);
  }
}
