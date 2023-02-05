# Depth-First Search, Breadth-First Search, Graph, Topological Sort
# Amazon 40 Google 5 Facebook 3 Intuit 3 Apple 3 TikTok 3 Uber 2 Coupang 2 Adobe 2 Palantir Technologies 2 ByteDance 2
# Coinbase 2 Microsoft 9 Bloomberg 3 Oracle 2 Salesforce 2 Tesla 2 Qualtrics 2 Citadel 2 Wayfair 2 Twitch 2 Karat 6
# Twilio 5 Snapchat 4 Robinhood 4 DoorDash 3 eBay 3 Splunk 3 Wish 3 Zillow 3 JPMorgan 2 HBO 2 C3 IoT 2 Nvidia 2
# VMware 2 Walmart Global Tech 2 Yelp Zenefits
# https://leetcode.com/problems/course-schedule/description/

# There are a total of course_count courses you have to take, labeled from 0 to course_count - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi
# first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:
# Input: course_count = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:
# Input: course_count = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
# All the pairs prerequisites[i] are unique.

class CourseSchedule:
    def canFinish(self, course_count: int, prerequisites: List[List[int]]) -> bool:
        pre_to_nexts: Dict[int, List[int]] = dict()
        for course in range(course_count):
            pre_to_nexts[course] = list()

        indegrees = [0 for _ in range(0, course_count)]
        for course, pre in prerequisites:
            pre_to_nexts.get(pre).append(course)
            indegrees[course] += 1

        queue = deque()
        for course in range(0, course_count):
            if indegrees[course] == 0:
                queue.append(course)

        count = 0
        while queue:
            pre = queue.popleft()
            count += 1
            next_courses = pre_to_nexts.get(pre)
            for course in next_courses:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    queue.append(course)

        return count == course_count
