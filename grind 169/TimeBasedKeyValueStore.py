# Hash Table, String, Binary Search, Design
# https://leetcode.com/problems/time-based-key-value-store
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps
# and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously,
# with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with
# the largest timestamp_prev. If there are no values, it returns "".
class TimeMap:

    def __init__(self):
        self.key_to_val_time_pair = dict()  # Dict[str, List[Tuple[str, int]]]

    def set(self, key: str, value: str, time: int) -> None:
        if key not in self.key_to_val_time_pair:
            self.key_to_val_time_pair[key] = list()

        self.key_to_val_time_pair[key].append((value, time))

    def get(self, key: str, max_time: int) -> str:
        if key not in self.key_to_val_time_pair:
            return ""
        val_time_pairs = self.key_to_val_time_pair[key]
        # NOTE: All the timestamps timestamp of set are strictly increasing.
        # binary search a right bound smaller than max_time
        left = 0
        right = len(val_time_pairs) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            mid_time = val_time_pairs[mid][1]
            if mid_time == max_time:
                return val_time_pairs[mid][0]
            elif mid_time > max_time:
                right = mid
            elif mid_time < max_time:
                left = mid

        if val_time_pairs[right][1] <= max_time:
            return val_time_pairs[right][0]

        if val_time_pairs[left][1] <= max_time:
            return val_time_pairs[left][0]

        return ""  # not found

    # def get(self, key: str, max_time: int) -> str:
    #     if key not in self.key_to_val_time_pair:
    #         return ""
    #     val_time_pairs = self.key_to_val_time_pair[key]
    #     # NOTE: All the timestamps timestamp of set are strictly increasing.
    #     # so loop from end to start
    #     for i in range(len(val_time_pairs) - 1, -1, -1):
    #         val, time = val_time_pairs[i]
    #         if time <= max_time:
    #             return val

    #     return "" # not found
