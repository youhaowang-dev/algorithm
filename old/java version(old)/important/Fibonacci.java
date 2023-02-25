// https://www.lintcode.com/problem/366/
class Fibonacci {

  public int fibonacci(int n) {
    if (n == 1) {
      return 0;
    }
    if (n == 2) {
      return 1;
    }

    int prevPrev = 0;
    int prev = 1;
    int result = 0;
    for (int i = 3; i < n + 1; i++) {
      result = prevPrev + prev;
      prevPrev = prev;
      prev = result;
    }

    return result;
  }
}
