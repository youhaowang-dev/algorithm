# Depth-First Search, Breadth-First Search, Graph, Topological Sort
# Amazon 25 Google 11 TikTok 8 Microsoft 6 Palantir Technologies 4 Apple 3 Roblox 3 ByteDance 3 Intuit 2 Robinhood 5 Facebook 4 Twilio 4 VMware 4 Salesforce 3 Coinbase 3 Snapchat 2 Uber 2 DoorDash 15 Karat 15 Bloomberg 5 Wayfair 5 Nutanix 4 Lyft 3 Goldman Sachs 3 Oracle 2 Pinterest 2 eBay 2 Adobe 2 Paypal 2 ServiceNow 2 Zenefits
# https://leetcode.com/problems/course-schedule-ii/
# There are a total of course_count courses you have to take, labeled from 0 to course_count - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
# Example 1:
# Input: course_count = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
# Example 2:
# Input: course_count = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
# Example 3:
# Input: course_count = 1, prerequisites = []
# Output: [0]

class CourseScheduleII:
    def findOrder(self, course_count: int, next_course_pairs: List[List[int]]) -> List[int]:
        if not course_count:
            return [0]

        if not next_course_pairs:
            return [course for course in range(course_count)]

        course_to_nexts = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for next, course in next_course_pairs:
            course_to_nexts[course].append(next)
            indegrees[next] += 1

        queue = deque()
        for course in range(course_count):
            if indegrees[course] == 0:
                queue.append(course)

        results = list()
        while queue:
            courses = self.get_all_courses(queue)
            results.extend(courses)
            for course in courses:
                nexts = course_to_nexts[course]
                self.update_queue(nexts, indegrees, queue)

        # still need to check if can take all
        for indegree in indegrees.values():
            if indegree != 0:
                return list()

        return results

    def get_all_courses(self, queue):
        courses = list()
        while queue:
            courses.append(queue.popleft())

        return courses

    def update_queue(self, nexts, indegrees, queue):
        for next in nexts:
            indegrees[next] -= 1
            if indegrees[next] == 0:
                queue.append(next)
