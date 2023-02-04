# Hash Table, String, Greedy, Sorting, Heap (Priority Queue), Counting
# https://leetcode.com/problems/reorganize-string
# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

# Example 1:
# Input: s = "aab"
# Output: "aba"
# Example 2:
# Input: s = "aaab"
# Output: ""

# "aaabbc"
# prev_used (-3, 'a') current (-2, 'b') result ['a', 'b']
# prev_used (-2, 'b') current (-2, 'a') result ['a', 'b', 'a']
# prev_used (-2, 'a') current (-1, 'b') result ['a', 'b', 'a', 'b']
# prev_used (-1, 'b') current (-1, 'a') result ['a', 'b', 'a', 'b', 'a']
# prev_used (-1, 'a') current (-1, 'c') result ['a', 'b', 'a', 'b', 'a', 'c']
# "aaab"
# prev_used (-3, 'a') current (-1, 'b') result ['a', 'b']
# prev_used (-1, 'b') current (-2, 'a') result ['a', 'b', 'a']
# greedy, pick the char with highest count, append to result, save to prev(we don't append same char)
# O(nlogn) for n heappush and heappop
class ReorganizeString:
    def reorganizeString(self, input_string: str) -> str:
        if input_string == "":
            return ""

        # create a counter
        char_to_count = collections.Counter(input_string)

        min_heap = [(-count, char) for char, count in char_to_count.items()]
        heapq.heapify(min_heap)  # O(n) for python

        result = list()
        # we don't append same char, so track it
        prev_used = heapq.heappop(min_heap)
        result.append(prev_used[1])
        while min_heap:
            current = heapq.heappop(min_heap)
            result.append(current[1])
            # print("prev_used", prev_used, "current", current, "result", result)
            prev_count, prev_char = prev_used
            prev_used = current
            if prev_count + 1:  # reduce negative, so +1
                heapq.heappush(min_heap, (prev_count + 1, prev_char))

        if len(result) == len(input_string):
            return "".join(result)

        return ""
