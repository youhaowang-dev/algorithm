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

# topological sort, time course_count^2 for dense graph, space course_count^2 for dense graph
class CourseSchedule:
    def canFinish(self, course_count: int, next_course_pairs: List[List[int]]) -> bool:
        if not course_count or not next_course_pairs:
            return True

        course_to_nexts = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for next, course in next_course_pairs:
            course_to_nexts[course].append(next)
            indegrees[next] += 1

        queue = deque()
        # no need to dedup as 0 indegree can only happen once unless bad input
        # for course, indegree in indegrees.items(): # wont work because items has no default key
        for course in range(course_count):
            if indegrees[course] == 0:
                queue.append(course)

        while queue:
            courses = self.get_all_courses(queue)
            for course in courses:
                self.update_next_courses(
                    course_to_nexts[course], queue, indegrees)

        for indegree in indegrees.values():
            if indegree != 0:
                return False

        return True

    def get_all_courses(self, queue):
        courses = list()
        while queue:
            courses.append(queue.popleft())

        return courses

    def update_next_courses(self, nexts, queue, indegrees):
        for next in nexts:
            indegrees[next] -= 1
            if indegrees[next] == 0:
                queue.append(next)
