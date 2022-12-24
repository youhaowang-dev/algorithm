// https://www.lintcode.com/problem/143/description
// Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.
// Example1
// Input:
// [3,2,2,1,4]
// 4
// Output:
// [1,2,2,3,4]
// Example2
// Input:
// [2,1,1,2,2]
// 2
// Output:
// [1,1,2,2,2]

// Challenge
// You can directly use The counting sorting algorithm scan twice, but it will cost O(k) extra memory. Now can you do it in use O(logk) extra memory?
public class SortColorsII {

  public void sortColors2(int[] colors, int k) {
    if (colors == null || colors.length < 2) {
      return;
    }

    this.sort(colors, 0, colors.length - 1, 1, k);
  }

  private void sort(
    int[] colors,
    int start,
    int end,
    int colorFrom,
    int colorTo
  ) {
    if (start >= end || colorFrom == colorTo) {
      return;
    }

    int left = start;
    int right = end;
    int colorMid = (colorFrom + colorTo) / 2;

    while (left <= right) {
      while (left <= right && colors[left] <= colorMid) {
        left++;
      }
      while (left <= right && colors[right] > colorMid) {
        right--;
      }
      if (left <= right) {
        int leftCopy = colors[left];
        colors[left] = colors[right];
        colors[right] = leftCopy;
      }
    }

    this.sort(colors, start, right, colorFrom, colorMid);
    this.sort(colors, left, end, colorMid + 1, colorTo);
  }
}
