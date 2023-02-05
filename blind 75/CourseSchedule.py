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

# bfs, build course_to_require_count, enqueue 0 course and reduce count by 1 for next
# {4: 0, 1: 1, 2: 1, 3: 2}, deque([4])
# {4: 0, 1: 0, 2: 0, 3: 2}, deque([1, 2])
# {4: 0, 1: 0, 2: 0, 3: 1}, deque([2])
# {4: 0, 1: 0, 2: 0, 3: 0}, deque([3])
# {4: 0, 1: 0, 2: 0, 3: 0}, deque([])
class CourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        course_to_nexts = dict()
        course_to_required_count = dict()
        for next_course, course in prerequisites:
            if course not in course_to_nexts:
                course_to_nexts[course] = list()
            course_to_nexts[course].append(next_course)

            if course not in course_to_required_count:  # no prerequisite, but need for init
                course_to_required_count[course] = 0

            if next_course not in course_to_required_count:
                course_to_required_count[next_course] = 1
            else:
                course_to_required_count[next_course] += 1

        queue = deque()
        for course, require_count in course_to_required_count.items():
            if require_count == 0:
                queue.append(course)
        while queue:
            course = queue.popleft()
            next_courses = course_to_nexts.get(course, list())
            for next_course in next_courses:
                course_to_required_count[next_course] -= 1
                if course_to_required_count[next_course] == 0:
                    queue.append(next_course)

        for require_count in course_to_required_count.values():
            if require_count != 0:
                return False

        return True
