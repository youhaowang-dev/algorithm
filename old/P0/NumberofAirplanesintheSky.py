# Amazon
# https://www.lintcode.com/problem/391/

# Given an list interval, which are taking off and landing time of the flight.
# How many airplanes are there at most at the same time in the sky?
# If landing and taking off of different planes happen at the same time, we consider landing should happen at first.

# Example 1:
# Input: [(1, 10), (2, 3), (5, 8), (4, 7)]
# Output: 3
# Explanation:
# The first airplane takes off at 1 and lands at 10.
# The second ariplane takes off at 2 and lands at 3.
# The third ariplane takes off at 5 and lands at 8.
# The forth ariplane takes off at 4 and lands at 7.
# During 5 to 6, there are three airplanes in the sky.

# Example 2:
# Input: [(1, 2), (2, 3), (3, 4)]
# Output: 1
# Explanation: Landing happen before taking off.

from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Operation:
    LAND = "LAND"
    TAKEOFF = "TAKEOFF"

    def __init__(self, time: int, operation: str):
        self.time = time
        self.operation = operation

    def __lt__(self, other):
        if self.time == other.time:
            return self.operation == self.LAND

        return self.time < other.time


# put start timestamp and end timestamp in list and sort ASC
# for each timestamp, count+1 if is start, count-1 if is end, while keep max_count = max(max_count, current_count)
class Solution:
    def count_of_airplanes(self, airplanes: List[Interval]) -> int:
        time_operations = list()
        for airplane in airplanes:
            time_operations.append(Operation(airplane.start, Operation.TAKEOFF))
            time_operations.append(Operation(airplane.end, Operation.LAND))

        sorted_time_operations = sorted(time_operations)

        count = 0
        max_count = 0
        for operation in sorted_time_operations:
            if operation.operation == Operation.TAKEOFF:
                count += 1
            if operation.operation == Operation.LAND:
                count -= 1

            max_count = max(max_count, count)

        return max_count
