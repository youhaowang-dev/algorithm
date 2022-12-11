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

  public double myPow(double base, int power) {
    return 0.001;
  }

  public static void main(String[] args) throws Exception {
    Pow Pow = new Pow();
    double[] bases = new double[] { 2.0000, 2.1000 };
    int power = 10;
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] { "myPow" };

    for (double base : bases) {
      for (String methodName : testMethodNames) {
        java.lang.reflect.Method method = Pow
          .getClass()
          .getMethod(methodName, double.class, int.class);
        double result = (double) method.invoke(Pow, base, power);

        System.out.println(
          String.format(
            "Method Name: %s\nInput: %s, Output: %s",
            methodName,
            "Base: " + base + "Power: " + power,
            result
          )
        );
      }
    }
  }
}
