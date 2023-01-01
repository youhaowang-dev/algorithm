// Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree
// Amazon 6 Microsoft 3 Apple 2 Adobe 2 Yahoo 2 Oracle 2 Facebook 8 Google 3 Bloomberg 2 Airbnb
// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

// Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

class ConvertSortedArraytoBinarySearchTree {

  public TreeNode sortedArrayToBST(int[] nums) {
    if (nums == null || nums.length == 0) {
      return null;
    }

    return this.buildBalancedBST(nums, 0, nums.length - 1);
  }

  private TreeNode buildBalancedBST(int[] nums, int left, int right) {
    if (left > right) {
      return null;
    }

    int mid = left + (right - left) / 2; // (left + right) / 2;
    TreeNode root = new TreeNode(nums[mid]);
    root.left = this.buildBalancedBST(nums, left, mid - 1);
    root.right = this.buildBalancedBST(nums, mid + 1, right);

    return root;
  }

  // bfs
  class Range {

    int start, end;
    TreeNode root;

    public Range(int start, int end, TreeNode root) {
      this.start = start;
      this.end = end;
      this.root = root;
    }
  }

  public TreeNode sortedArrayToBST(int[] nums) {
    TreeNode root = null;
    if (nums == null || nums.length == 0) {
      return root;
    }

    Queue<Range> queue = new LinkedList<>();
    queue.offer(new Range(0, nums.length - 1, null));
    while (!queue.isEmpty()) {
      Range range = queue.poll();
      if (range.start > range.end) continue;
      int mid = (range.start + range.end) / 2;
      TreeNode node = new TreeNode(nums[mid]);
      // 3 cases
      // 1. no root, so node becomes root
      // 2. has root and node is smaller, so it is left
      // 2. has root and node is bigger, so it is right
      if (range.root == null) {
        root = node;
      } else {
        if (node.val < range.root.val) {
          range.root.left = node;
        } else {
          range.root.right = node;
        }
      }
      queue.offer(new Range(range.start, mid - 1, node));
      queue.offer(new Range(mid + 1, range.end, node));
    }
    return root;
  }
}
