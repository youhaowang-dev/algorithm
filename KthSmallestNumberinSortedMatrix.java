// https://www.lintcode.com/problem/401/description

// Find the kth smallest number in a row and column sorted matrix.
// The sorting matrix is defined as: each row is incremented and each column is incremented.
// Example 1:
// Input:
// [
//   [1 ,5 ,7],
//   [3 ,7 ,8],
//   [4 ,8 ,9],
// ]
// k = 4
// Output: 5
// Example 2:
// Input:
// [
//   [1, 2],
//   [3, 4]
// ]
// k = 3
// Output: 3
// Challenge
// O*(klogn*) time, n is the maximum of the width and height of the matrix.
class KthSmallestNumberinSortedMatrix {

  // minHeap check the first element row by row for k times
  public int kthSmallest(int[][] matrix, int k) {
    // write your code here
    PriorityQueue<Node> minHeap = new PriorityQueue<Node>((Node a, Node b) ->
      (a.value - b.value)
    );

    for (int rowIndex = 0; rowIndex < matrix.length; rowIndex++) {
      minHeap.add(new Node(matrix[rowIndex][0], rowIndex, 0));
    }
    int count = 0;
    while (count < k - 1) {
      Node top = minHeap.poll();
      int rowIndex = top.rowIndex;
      int colIndex = top.colIndex;
      if (colIndex + 1 < matrix[0].length) {
        minHeap.add(
          new Node(matrix[rowIndex][colIndex + 1], rowIndex, colIndex + 1)
        );
      }
      count++;
    }

    return minHeap.poll().value;
  }
}

class Node {

  int value;
  int rowIndex;
  int colIndex;

  public Node(int value, int rowIndex, int colIndex) {
    this.value = value;
    this.rowIndex = rowIndex;
    this.colIndex = colIndex;
  }
}
