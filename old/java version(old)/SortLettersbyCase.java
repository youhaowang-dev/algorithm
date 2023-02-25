// https://www.lintcode.com/problem/49/description
// Given a string chars which contains only letters. Sort it by lower case first and upper case second.
// In different languages, chars will be given in different ways. For example, the string "abc" will be given in following ways:

// Java: char[] chars = {'a', 'b', 'c'};
// Python：chars = ['a', 'b', 'c']
// C++：string chars = "abc";
// You need to implement the in-place algorithm to solve this problem without returning any values, and we will determine if your result is correct based on the sorted chars.

// Example 1:
// Input:
// chars = "abAcD"
// Output:
// "acbAD"
// Explanation:
// You can also return "abcAD" or "cbaAD" or other correct answers.
// Example 2:
// Input:
// chars = "ABC"
// Output:
// "ABC"
// Explanation:
// You can also return "CBA" or "BCA" or other correct answers.

// Challenge
// Do it in one-pass and in-place.
class SortLettersbyCase {

  public void sortLetters(char[] chars) {
    int left = 0;
    int right = chars.length - 1;
    while (left <= right) {
      while (left <= right && Character.isLowerCase(chars[left])) {
        left++;
      }
      while (left <= right && Character.isUpperCase(chars[right])) {
        right--;
      }
      if (left <= right) {
        char leftCopy = chars[left];
        chars[left] = chars[right];
        chars[right] = leftCopy;
        left++;
        right--;
      }
    }
  }
}
