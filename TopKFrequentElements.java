// Amazon 24 Facebook 11 Google 5 Microsoft 4 Apple 4 Bloomberg 3 Uber 3 Adobe 2 ByteDance 2 Tesla 2 Oracle 5 Snapchat 3 Indeed 3 Cisco 3 Netflix 3 Shopee 3 Twitter 2 Yahoo 2 eBay 2 VMware 2 TikTok 2 Arcesium 2 Deloitte 2 Yelp 6 Walmart Global Tech 6 Capital One 5 Salesforce 3 HBO 3 LinkedIn 2 Dropbox 2 Expedia 2 Twilio 2 Paypal 2 Wish 2 C3 IoT 2 Zynga 2 Cashfree 2 Pocket Gems
// Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect

// https://leetcode.com/problems/top-k-frequent-elements/description/

// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

// Example 1:
// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]
// Example 2:
// Input: nums = [1], k = 1
// Output: [1]

// Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

class TopKFrequentElements {

  // partition the array O(n)
  // If by chance our pivot element took N - kth final position,
  // then k elements on the right are these top k frequent we're looking for.
  // If not, we can choose one more pivot and place it in its perfect position.
  public int[] topKFrequent(int[] nums, int k) {
    Map<Integer, Integer> count = new HashMap();
    for (int num : nums) {
      count.put(num, count.getOrDefault(num, 0) + 1);
    }

    int n = count.size();
    int[] unique = new int[n];
    int i = 0;
    for (int num : count.keySet()) {
      unique[i] = num;
      i++;
    }

    // kth top frequent element is (n - k)th less frequent.
    // Do a partial sort: from less frequent to the most frequent, till
    // (n - k)th less frequent element takes its place (n - k) in a sorted array.
    // All element on the left are less frequent.
    // All the elements on the right are more frequent.
    this.quickselect(unique, count, 0, n - 1, n - k);
    // Return top k frequent elements
    return Arrays.copyOfRange(unique, n - k, n);
  }

  public void swap(int a, int b, int[] nums) {
    int tmp = nums[a];
    nums[a] = nums[b];
    nums[b] = tmp;
  }

  public int partition(
    int[] unique,
    Map<Integer, Integer> count,
    int start,
    int end,
    int pivotIndex
  ) {
    int pivotCount = count.get(unique[pivotIndex]);
    // 1. move pivot to end
    this.swap(pivotIndex, end, unique);
    int sortedPivotIndex = start;

    // 2. move all less frequent elements to the start
    for (int i = start; i <= end; i++) {
      if (count.get(unique[i]) < pivotCount) {
        this.swap(sortedPivotIndex, i, unique);
        sortedPivotIndex++;
      }
    }

    // 3. move pivot to its final place
    this.swap(sortedPivotIndex, end, unique);

    return sortedPivotIndex;
  }

  public void quickselect(
    int[] unique,
    Map<Integer, Integer> count,
    int start,
    int end,
    int targetIndex
  ) {
    if (start == end) {
      return;
    }

    int pivotIndex = (end + start) / 2;

    // find the pivot position in a sorted list
    int sortedPivotIndex =
      this.partition(unique, count, start, end, pivotIndex);

    // if the pivot is in its final sorted position
    if (targetIndex == sortedPivotIndex) {
      return;
    } else if (targetIndex < sortedPivotIndex) {
      // go start
      this.quickselect(unique, count, start, sortedPivotIndex - 1, targetIndex);
    } else {
      // go end
      this.quickselect(unique, count, sortedPivotIndex + 1, end, targetIndex);
    }
  }

  // maintain a heap with size k, make sure higher frequency nums are not at the peek -> minHeap
  // time O(nlogk)
  public int[] topKFrequent(int[] nums, int k) {
    // build count
    Map<Integer, Integer> numToCount = new HashMap<>();
    for (int num : nums) {
      numToCount.putIfAbsent(num, 0);
      numToCount.put(num, 1 + numToCount.get(num));
    }

    // build minHeap
    Queue<Integer> minHeap = new PriorityQueue<>((a, b) ->
      numToCount.get(a) - numToCount.get(b)
    );
    for (int num : numToCount.keySet()) {
      minHeap.offer(num);
      if (minHeap.size() > k) {
        minHeap.poll();
      }
    }

    // build result
    int heapSize = minHeap.size();
    int[] result = new int[heapSize];
    // NOTE: i < minHeap.size() wont work as the size reduces
    // for (int i = 0; i < minHeap.size(); i++) {
    for (int i = 0; i < heapSize; i++) {
      result[i] = minHeap.poll();
    }

    return result;
  }
}
