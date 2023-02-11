# https://leetcode.com/problems/task-scheduler/
# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different
# task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could
# complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same l
# etter in the array), that is that there must be at least n units of time between any two same tasks.

# Return the least number of units of times that the CPU will take to finish all the given tasks.

# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.

# use queue and min heap, put(task count, next available time)
# time O(n * len(tasks)), case like [a,a,a,a] and 4
class TaskScheduler:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_to_count = collections.Counter(tasks)
        min_heap = [-count for count in task_to_count.values()]
        heapq.heapify(min_heap)

        time = 0  # timestamp
        queue = collections.deque()  # Tuple[task count, next available time]
        while min_heap or queue:
            time += 1  # increase time
            if min_heap:  # poll the most count and add to queue
                count = 1 + heapq.heappop(min_heap)  # update count
                if count != 0:
                    queue.append((count, time + n))
            if queue and queue[0][1] == time:  # poll the task and add to heap
                heapq.heappush(min_heap, queue.popleft()[0])

        return time
