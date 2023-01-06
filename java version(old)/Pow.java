// Math, Recursion, Binary Search
// Facebook 15 Apple 6 Amazon 5 Google 4 Microsoft 4 Yahoo 4 Bloomberg 3 LinkedIn 2 Uber 2 Paypal 2
// 50. Pow(x, n)
// https://leetcode.com/problems/powx-n/
// Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

// Example 1:
// Input: x = 2.00000, n = 10
// Output: 1024.00000

// Example 2:
// Input: x = 2.10000, n = 3
// Output: 9.26100

// Example 3:
// Input: x = 2.00000, n = -2
// Output: 0.25000
// Explanation: 2-2 = 1/22 = 1/4 = 0.25

final class Pow {

  // power can be 2^a+2^b+2^c+...
  // when n % 2 == 1, mutiply the answer by current_product because / will remove one
  // do current_product = base * base n times
  public double myPow(double base, int power) {
    long currentPower = power; // -power may overflow
    if (currentPower < 0) {
      base = 1 / base;
      currentPower = -currentPower;
    }
    double result = 1;
    double current_product = base;
    while (currentPower > 0) {
      if (currentPower % 2 == 1) {
        result = result * current_product;
      }
      current_product = current_product * current_product;
      currentPower = currentPower / 2;
    }

    return result;
  }

  public static void main(String[] args) throws Exception {
    Pow Pow = new Pow();
    double[] bases = new double[] { 2.0000, 2.1000 };
    // int power = 10;
    int power = -2;
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] { "myPow" };

    for (double base : bases) {
      for (String methodName : testMethodNames) {
        java.lang.reflect.Method method = Pow
          .getClass()
          .getMethod(methodName, double.class, int.class);
        double result = (double) method.invoke(Pow, base, power);
        System.out.println("methodName: " + methodName);
        System.out.println("base: " + base);
        System.out.println("power: " + power);
        System.out.println("result: " + result);
        System.out.println();
      }
    }
  }
}
