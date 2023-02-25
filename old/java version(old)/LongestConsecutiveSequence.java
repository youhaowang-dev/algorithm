// Array, Hash Table, Union Find
// Google 11 Amazon 10 Adobe 5 Apple 5 Bloomberg 4 Facebook 2 Microsoft 2 Spotify 4 Visa 2 Qualtrics 2 eBay 2 Morgan Stanley 2 LinkedIn 4 Zillow 3 Goldman Sachs 3 Salesforce 3 Uber 2 Cohesity 2 Twitter 2 Cisco 2
// https://leetcode.com/problems/longest-consecutive-sequence/description/

// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
// You must write an algorithm that runs in O(n) time.
//
// Example 1:
// Input: nums = [100,4,200,1,3,2]
// Output: 4
// Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
// Example 2:
// Input: nums = [0,3,7,2,5,8,4,6,0,1]
// Output: 9
class LongestConsecutiveSequence {

  // better brute force O(n)
  // the inner while loop only runs with head of a sequence, so the while can only check n elements in total
  // the total complexity is O(n + n) for the for-while loop, so O(n)
  public int longestConsecutive(int[] nums) {
    Set<Integer> numsSet = new HashSet<>();
    for (int num : nums) {
      numsSet.add(num);
    }

    int longestSequenceLength = 0;
    for (int num : numsSet) {
      int prevNum = num - 1;
      if (numsSet.contains(prevNum)) {
        // skip if num is in the mid of sequence
        continue;
      }

      int currentSequenceLength = 1;
      int nextNum = num + 1;
      while (numsSet.contains(nextNum)) {
        currentSequenceLength++;
        nextNum++;
      }
      longestSequenceLength =
        Math.max(longestSequenceLength, currentSequenceLength);
    }

    return longestSequenceLength;
  }

  // brute force O(n^3)
  public int longestConsecutive(int[] nums) {
    int longestConsecutive = 0;

    for (int num : nums) {
      int currentNum = num;
      int currentConsecutive = 1;

      while (this.hasNextConsecutive(nums, currentNum + 1)) {
        currentNum += 1;
        currentConsecutive += 1;
      }

      longestConsecutive = Math.max(longestConsecutive, currentConsecutive);
    }

    return longestConsecutive;
  }

  private boolean hasNextConsecutive(int[] nums, int nextConsecutive) {
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] == nextConsecutive) {
        return true;
      }
    }

    return false;
  }
}
