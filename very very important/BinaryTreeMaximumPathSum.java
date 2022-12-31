// Dynamic Programming, Tree, Depth-First Search, Binary Tree
// DoorDash 23 Microsoft 5 Amazon 4 Facebook 3 Bloomberg 2 Adobe 2 Apple 2 Samsung 2 TikTok 2 Akuna Capital 2 Google 8 ByteDance 6 Snapchat 3 Oracle 2 Twitter 2 Twilio 2 Yandex 2 Sprinklr 2 TuSimple 2
// https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

// A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has
// an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

// The path sum of a path is the sum of the node's values in the path.

// Given the root of a binary tree, return the maximum path sum of any non-empty path.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class BinaryTreeMaximumPathSum {

  private class PathSums {

    int rootToAny;
    int anyToAny;

    public PathSums(int rootToAny, int anyToAny) {
      this.rootToAny = rootToAny;
      this.anyToAny = anyToAny;
    }
  }

  // divide and conquer: time O(n)
  // two types of paths: rootToAny and anyToAny
  // max(rootToAny) = root.val + max(left rootToAny, right rootToAny)
  // max(anyToAny) = max(left anyToAny, right anyToAny, current anyToAny)
  //      current anyToAny passes the root = root.val + max(0, left anyToAny) + max(0, right anyToAny)
  // rootToAny/anyToAny can be negative, so max(0, rootToAny/anyToAny) is needed because we don't have to take subtree paths
  //
  public int maxPathSum(TreeNode root) {
    return this.getMaxPathSum(root).anyToAny;
  }

  private PathSums getMaxPathSum(TreeNode root) {
    // exit
    if (root == null) {
      return new PathSums(Integer.MIN_VALUE, Integer.MIN_VALUE);
    }

    // divide
    PathSums leftVals = this.getMaxPathSum(root.left);
    PathSums rightVals = this.getMaxPathSum(root.right);

    // merge
    int maxSubtreeRootToAny = Math.max(
      0,
      Math.max(leftVals.rootToAny, rightVals.rootToAny)
    );
    int maxCurrentRootToAny = root.val + maxSubtreeRootToAny;

    int maxSubtreeAnyToAny = Math.max(leftVals.anyToAny, rightVals.anyToAny);
    int currentRootAnyToAny =
      root.val +
      Math.max(0, leftVals.rootToAny) +
      Math.max(0, rightVals.rootToAny);
    int maxCurrentAnyToAny = Math.max(maxSubtreeAnyToAny, currentRootAnyToAny);

    return new PathSums(maxCurrentRootToAny, maxCurrentAnyToAny);
  }

  // brute force
  // time complexity: O(N*N*logN)
  Map<TreeNode, TreeNode> map;

  public int maxPathSum(TreeNode root) {
    if (root == null) return 0;
    map = new HashMap<>();
    map.put(root, null);
    traverse(root); // traverse all nodes and create a map of ancestors (similar to common ancestor problem)
    List<TreeNode> list = new ArrayList<>();
    for (TreeNode node : map.keySet()) {
      // System.out.println(node.val);
      list.add(node); // converting keys to a list for bruteforcing
    }
    int max = Integer.MIN_VALUE;
    for (int i = 0; i < list.size(); i++) {
      for (int j = i; j < list.size(); j++) { // j=i as in the path there could be only 1 node.
        max = Math.max(max, findSum(list.get(i), list.get(j)));
      }
    }
    return max;
  }

  /**
	TC: Log(N) in worst-case.
	Idea is to find the path from both src & dest to a common ancestor. 
	The common ancestor can be src or dest too.
	Or src can be same as dest.
	**/
  public int findSum(TreeNode src, TreeNode dest) {
    Map<TreeNode, Integer> sumMap = new HashMap<>(); // keep track of sum at each ancestor/node , starting from the src.
    int sum = 0;
    Set<TreeNode> visited = new HashSet<>();
    while (src != null) {
      sum += src.val; // this computes path sum from src to the common ancestor.

      sumMap.put(src, sum);
      visited.add(src);
      src = map.get(src);
    }
    sum = 0;

    //Now We just need to compute sum from dest till  common_ancetor-1
    while (dest != null && !visited.contains(dest)) {
      sum += dest.val;
      dest = map.get(dest);
    }

    return dest == null ? sum : sum + sumMap.get(dest);
  }

  public void traverse(TreeNode node) {
    if (node != null) {
      if (node.left != null) {
        map.put(node.left, node);
      }
      traverse(node.left);
      traverse(node.right);
      if (node.right != null) {
        map.put(node.right, node);
      }
    }
  }
}
