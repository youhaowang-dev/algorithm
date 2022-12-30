class MinimumDepthofBinaryTree {

  // recursive dfs
  public int minDepth(TreeNode root) {
    if (root == null) {
      return 0;
    }

    // one of the subtree condition
    if (root.left == null && root.right == null) {
      return 1;
    }

    int minDepth = Integer.MAX_VALUE;
    // null condition check is needed for Math.min, otherwise unbalanced tree will not return the depth
    // without null check the very unbalanced tree(list) will return 1
    if (root.left != null) {
      minDepth = Math.min(minDepth(root.left), minDepth);
    }
    if (root.right != null) {
      minDepth = Math.min(minDepth(root.right), minDepth);
    }

    return minDepth + 1;
  }

  // iterative dfs
  // Pair is a KV Java tuple, getKey() getValue()
  public int minDepth(TreeNode root) {
    LinkedList<Pair<TreeNode, Integer>> stack = new LinkedList<>();
    if (root == null) {
      return 0;
    } else {
      stack.push(new Pair(root, 1));
    }

    int minDepth = Integer.MAX_VALUE;
    while (!stack.isEmpty()) {
      Pair<TreeNode, Integer> current = stack.pop();
      TreeNode node = current.getKey();
      int currentDepth = current.getValue();
      if (node.left == null && node.right == null) {
        minDepth = Math.min(minDepth, currentDepth);
      }
      if (node.left != null) {
        stack.push(new Pair(node.left, currentDepth + 1));
      }
      if (node.right != null) {
        stack.push(new Pair(node.right, currentDepth + 1));
      }
    }

    return minDepth;
  }
}
