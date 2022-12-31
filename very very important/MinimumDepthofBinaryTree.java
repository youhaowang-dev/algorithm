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

  // max depth: keep going until last level
  // min depth: min is found when left==null && right==null
  public int minDepth(TreeNode root) {
    int depth = 0;
    if (root == null) {
      return depth;
    }
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    while (!queue.isEmpty()) {
      depth++;
      int levelNodeCount = queue.size();
      for (int i = 0; i < levelNodeCount; i++) {
        TreeNode node = queue.poll();
        if (node.left == null && node.right == null) {
          // found min
          return depth;
        }
        if (node.left != null) {
          queue.offer(node.left);
        }
        if (node.right != null) {
          queue.offer(node.right);
        }
      }
    }

    return depth;
  }

  // iterative dfs
  // Pair is a KV Java tuple, getKey() getValue()
  public int minDepth(TreeNode root) {
    Stack<Pair<TreeNode, Integer>> stack = new Stack<>();
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
      // min depth requires this check for unbalanced tree
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
