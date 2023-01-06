public class CircularDeque {

  private int[] nums;
  private int left;
  private int right;
  private int size;

  public CircularDeque(int n) {
    nums = new int[n];
    left = 0;
    right = nums.length - 1;
    size = 0;
  }

  public boolean isFull() {
    return size == nums.length;
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public void pushFront(int element) {
    if (this.isFull()) {
      return;
    }

    left -= 1;
    if (left < 0) {
      left += nums.length;
    }
    size++;
    nums[left] = element;
  }

  public int popFront() {
    if (this.isEmpty()) {
      return -1; // throw
    }

    int val = nums[left];
    left = (left + 1) % nums.length;
    size--;
    return val;
  }

  public void pushBack(int element) {
    if (this.isFull()) {
      return;
    }

    right = (right + 1) % nums.length;
    nums[right] = element;
    size++;
  }

  public int popBack() {
    if (this.isEmpty()) {
      return -1;
    }

    int val = nums[right];
    right -= 1;
    if (right < 0) {
      right += nums.length;
    }
    size--;
    return val;
  }
}
