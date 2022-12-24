// https://www.lintcode.com/problem/955/
// Implement queue by circulant array. You need to support the following methods:
// CircularQueue(n): initialize a circular array with size n to store elements
// boolean isFull(): return true if the array is full
// boolean isEmpty(): return true if there is no element in the array
// void enqueue(element): add an element to the queue
// int dequeue(): pop an element from the queue

public class CircularQueue {

  int[] nums;
  int first;
  int last;
  int size;

  public CircularQueue(int n) {
    this.nums = new int[n];
    this.first = 0;
    this.last = 0;
    this.size = 0;
  }

  public boolean isFull() {
    return this.size == this.nums.length;
  }

  public boolean isEmpty() {
    return this.size == 0;
  }

  public void enqueue(int element) {
    this.last = (this.first + this.size) % this.nums.length;
    nums[last] = element;
    this.size++;
  }

  public int dequeue() {
    int number = this.nums[first];
    first = (first + 1) % this.nums.length;
    this.size--;
    return number;
  }
}
