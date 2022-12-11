// tag: Math, Binary Search
// Amazon 6 Bloomberg 4 Apple 4 Microsoft 3 Facebook 2 Google 2 LinkedIn 11 Adobe 6 Uber 2
// source: https://leetcode.com/problems/sqrtx/description/

// Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
// The returned integer should be non-negative as well.
// You must not use any built-in exponent function or operator.
// For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

// Example 1:
// Input: x = 4
// Output: 2
// Explanation: The square root of 4 is 2, so we return 2.

// Example 2:
// Input: x = 8
// Output: 2
// Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
import java.util.*;

final class Sqrt {

  public int sqrtInt(int x) {
    if (x <= 1) {
      return x;
    }

    int start = 1;
    int end = x;
    while (start + 1 < end) {
      int mid = start - (start - end) / 2;
      int dividedByMid = x / mid; // avoid mid * mid overflow
      if (dividedByMid == mid) {
        return mid;
      }
      if (dividedByMid < mid) {
        // mid too big; need to make it smaller
        end = mid;
      }
      if (dividedByMid > mid) {
        // mid too small; need to make it bigger
        start = mid;
      }
    }

    if (start <= x / start) {
      return start;
    }

    if (end <= x / end) {
      return end;
    }

    return Integer.MIN_VALUE; // throw new Exception();
  }

  public double sqrtDouble(int x, double precise) {
    double n = 0;
    while (((n + 1) * (n + 1)) <= x) {
      n++;
    }
    while ((n + precise) * (n + precise) <= x) {
      n += precise;
    }
    return n;
  }

  public static void main(String[] args) throws Exception {
    Sqrt Sqrt = new Sqrt();
    int[] targets = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 2147395599 };
    // NOTE: the method must be public to make .getMethod work
    String[] testMethodNames = new String[] { "sqrtInt" };

    for (int target : targets) {
      for (String methodName : testMethodNames) {
        java.lang.reflect.Method method = Sqrt
          .getClass()
          .getMethod(methodName, int.class);
        int sqrt = (int) method.invoke(Sqrt, target);

        System.out.println(
          String.format(
            "Method Name: %s\nInput: %s, Output: %s",
            methodName,
            target,
            sqrt
          )
        );
      }
    }

    String[] doubleSqrtMethods = new String[] { "sqrtDouble" };
    double precise = 0.001;
    for (int target : targets) {
      for (String methodName : doubleSqrtMethods) {
        java.lang.reflect.Method method = Sqrt
          .getClass()
          .getMethod(methodName, int.class, double.class);
        double sqrt = (double) method.invoke(Sqrt, target, precise);

        System.out.println(
          String.format(
            "Method Name: %s\nInput: %s, Output: %s",
            methodName,
            target,
            sqrt
          )
        );
      }
    }
  }
}
