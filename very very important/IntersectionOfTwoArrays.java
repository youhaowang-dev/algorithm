// Array, Hash Table, Two Pointers, Binary Search, Sorting
// Amazon 4 Apple 8 Google 7 Facebook 7 Bloomberg 4 Adobe 3 LinkedIn 6 Microsoft 5 Yahoo 2 JPMorgan 2 Yandex 2 VMware 2 Two Sigma Wix

// Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

// Example 1:
// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2]

// Example 2:
// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [9,4]
// Explanation: [4,9] is also accepted.

class IntersectionOfTwoArrays {

  // preprocess data for fast compare
  // compare two sets
  public int[] intersection(int[] nums1, int[] nums2) {
    Set<Integer> set1 = new HashSet<>();
    for (int num : nums1) {
      set1.add(num);
    }
    Set<Integer> set2 = new HashSet<>();
    for (int num : nums2) {
      set2.add(num);
    }

    Set<Integer> smallerSet;
    Set<Integer> biggerSet;
    if (set1.size() > set2.size()) {
      smallerSet = set2;
      biggerSet = set1;
    } else {
      smallerSet = set1;
      biggerSet = set2;
    }

    // IMPORTANT: java.util.ConcurrentModificationException
    // for (int num : smallerSet) {
    //   if (!biggerSet.contains(num)) {
    //     smallerSet.remove(num);
    //   }
    // }

    Set<Integer> resultSet = new HashSet<>();
    for (int num : smallerSet) {
      if (biggerSet.contains(num)) {
        resultSet.add(num);
      }
    }

    int[] result = new int[resultSet.size()];
    int index = 0;
    for (int num : resultSet) {
      result[index] = num;
      index++;
    }

    return result;
  }

  // brute force m*n
  public int[] intersection(int[] nums1, int[] nums2) {
    Set<Integer> intersection = new HashSet<>();
    for (int num1 : nums1) {
      for (int num2 : nums2) {
        // intersection.add
        if (num1 == num2) {
          intersection.add(num1);
        }
      }
    }

    int[] intersectionArray = new int[intersection.size()];
    int index = 0;
    for (int num : intersection) {
      intersectionArray[index] = num;
      index++;
    }

    return intersectionArray;
  }
}
