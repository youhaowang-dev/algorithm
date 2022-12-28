// Depth-First Search, Breadth-First Search, Graph, Topological Sort
// Amazon 40 Google 5 Facebook 3 Intuit 3 Apple 3 TikTok 3 Uber 2 Coupang 2 Adobe 2 Palantir Technologies 2 ByteDance 2 Coinbase 2 Microsoft 9 Bloomberg 3 Oracle 2 Salesforce 2 Tesla 2 Qualtrics 2 Citadel 2 Wayfair 2 Twitch 2 Karat 6 Twilio 5 Snapchat 4 Robinhood 4 DoorDash 3 eBay 3 Splunk 3 Wish 3 Zillow 3 JPMorgan 2 HBO 2 C3 IoT 2 Nvidia 2 VMware 2 Walmart Global Tech 2 Yelp Zenefits
// https://leetcode.com/problems/course-schedule/description/

// There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

// For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
// Return true if you can finish all courses. Otherwise, return false.

// Example 1:
// Input: numCourses = 2, prerequisites = [[1,0]]
// Output: true
// Explanation: There are a total of 2 courses to take.
// To take course 1 you should have finished course 0. So it is possible.
// Example 2:
// Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
// Output: false
// Explanation: There are a total of 2 courses to take.
// To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

// All the pairs prerequisites[i] are unique.
class CourseSchedule {

  public boolean canFinish(int numCourses, int[][] prerequisites) {
    Map<Integer, List<Integer>> courseToPres = new HashMap();
    for (int i = 0; i < numCourses; i++) {
      courseToPres.putIfAbsent(i, new ArrayList());
    }

    int[] indegrees = new int[numCourses];
    for (int[] courseToPre : prerequisites) {
      int course = courseToPre[0];
      int pre = courseToPre[1];
      courseToPres.get(course).add(pre);
      indegrees[pre]++;
    }

    Queue<Integer> queue = new LinkedList<Integer>();
    for (int i = 0; i < numCourses; i++) {
      if (indegrees[i] == 0) {
        queue.offer(i);
      }
    }

    int count = 0;
    while (!queue.isEmpty()) {
      int course = queue.poll();
      count++;
      List<Integer> pres = courseToPres.get(course);
      for (int pre : pres) {
        indegrees[pre]--;
        if (indegrees[pre] == 0) {
          queue.offer(pre);
        }
      }
    }

    return count == numCourses;
  }
}
