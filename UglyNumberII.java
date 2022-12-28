// Hash Table, Math, Dynamic Programming, Heap (Priority Queue)
// Adobe 2 Bloomberg 3 Microsoft 2

// An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

// Given an integer n, return the nth ugly number.

// Example 1:
// Input: n = 10
// Output: 12
// Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
// Example 2:
// Input: n = 1
// Output: 1
// Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

// IMPORTANT: ask interviewer overflow possibility
class UglyNumberII {

  // dp O(n)
  public int nthUglyNumber(int n) {
    int[] nums = new int[n];
    int index2 = 0;
    int index3 = 0;
    int index5 = 0;
    nums[0] = 1;
    for (int i = 1; i < nums.length; i++) {
      // this is like building the fibonacci numbers based on prev results
      nums[i] =
        Math.min(
          nums[index2] * 2,
          Math.min(nums[index3] * 3, nums[index5] * 5)
        );
      // so the multiplication order will be *2,*3,*5,*2,*3,*5,...
      if (nums[i] == nums[index2] * 2) {
        index2++;
      }
      if (nums[i] == nums[index3] * 3) {
        index3++;
      }
      if (nums[i] == nums[index5] * 5) {
        index5++;
      }
    }
    return nums[n - 1];
  }

  // minHeap where the top is the next number to * 2/3/5
  // from 1 construct the numbers, order matters because we need the nth
  // {1} peek = first number
  // 1 {2,3,5} peek = first number
  // 2 {3,5,4,6,10} peek = first number
  // need to dedup for 2*5 == 5*2
  public int nthUglyNumber(int n) {
    Queue<Integer> minHeap = new PriorityQueue<>();
    Set<Integer> seen = new HashSet<>();

    int[] primes = new int[] { 2, 3, 5 };
    for (int prime : primes) {
      minHeap.offer(prime);
      seen.add(prime);
    }

    int number = 1;
    for (int i = 1; i < n; i++) {
      // get next min
      number = minHeap.poll();
      for (int prime : primes) {
        int nextNumber = prime * number;
        if (!seen.contains(nextNumber)) {
          minHeap.offer(nextNumber);
          seen.add(nextNumber);
        }
      }
    }

    return number;
  }
}
