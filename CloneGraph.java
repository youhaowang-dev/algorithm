// Hash Table, Depth-First Search, Breadth-First Search, Graph
// Facebook 5 Amazon 4 Apple 3 Bloomberg 8 Google 5 Microsoft 3 Adobe 2 Pinterest 2 Salesforce 6 Twitter 3 Uber 3 Qualtrics 2 Oracle 2 Goldman Sachs 2 ByteDance 2 Pocket Gems Wix
// https://leetcode.com/problems/clone-graph/

// Given a reference of a node in a connected undirected graph.

// Return a deep copy (clone) of the graph.

// Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

// class Node {
//     public int val;
//     public List<Node> neighbors;
// }

// Test case format:

// For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

// An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

// The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class CloneGraph {

  public Node cloneGraph(Node node) {
    if (node == null) {
      return null;
    }
    // get all nodes as a list
    List<Node> nodes = this.getAllNodes(node);
    // copy nodes and map old to new in dict
    Map<Node, Node> oldToNew = this.copyNodes(nodes);
    // copy edges
    this.copyEdges(nodes, oldToNew);

    return oldToNew.get(node);
  }

  private List<Node> getAllNodes(Node node) {
    List<Node> nodes = new ArrayList<>();
    Set<Node> nodeSet = new HashSet<>();
    Queue<Node> queue = new LinkedList<>();
    queue.offer(node);

    while (!queue.isEmpty()) {
      Node current = queue.poll();
      if (nodeSet.contains(current)) {
        continue;
      }
      nodeSet.add(current);
      nodes.add(current);
      for (Node neighbor : current.neighbors) {
        queue.offer(neighbor);
      }
    }

    return nodes;
  }

  private Map<Node, Node> copyNodes(List<Node> nodes) {
    Map<Node, Node> oldToNew = new HashMap<>();
    for (Node node : nodes) {
      Node newNode = new Node(node.val);
      oldToNew.put(node, newNode);
    }

    return oldToNew;
  }

  private void copyEdges(List<Node> nodes, Map<Node, Node> oldToNew) {
    for (Node node : nodes) {
      Node newNode = oldToNew.get(node);
      for (Node neighbor : node.neighbors) {
        Node newNeighbor = oldToNew.get(neighbor);
        newNode.neighbors.add(newNeighbor);
      }
    }
  }
}
