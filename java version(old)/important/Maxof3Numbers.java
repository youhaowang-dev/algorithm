// https://www.lintcode.com/problem/283/description
// Given 3 integers, return the max of them.

class Maxof3Numbers {

  public int maxOfThreeNumbers(int num1, int num2, int num3) {
    return this.getMax(num1, this.getMax(num2, num3));
  }

  private int getMax(int num1, int num2) {
    if (num1 < num2) {
      return num2;
    } else {
      return num1;
    }
  }
}
