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
    Map<Integer, List<Integer>> preToCourses = new HashMap<>();
    for (int course = 0;  < numCourses; course++) {
      preToCourses.putIfAbsent(course, new ArrayList());
    }

    int[] indegrees = new int[numCourses];
    for (int[] coursePrePair : prerequisites) {
      int course = coursePrePair[0];
      int pre = coursePrePair[1];
      preToCourses.get(pre).add(course);
      indegrees[course]++;
    }

    Queue<Integer> queue = new LinkedList<Integer>();
    for (int course = 0; course < numCourses; course++) {
      if (indegrees[course] == 0) {
        queue.offer(course);
      }
    }

    int count = 0;
    while (!queue.isEmpty()) {
      int pre = queue.poll();
      count++;
      List<Integer> courses = preToCourses.get(pre);
      for (int course : courses) {
        indegrees[course]--;
        if (indegrees[course] == 0) {
          queue.offer(course);
        }
      }
    }

    return count == numCourses;
  }
}
