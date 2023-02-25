# String, Backtracking, Breadth-First Search
# Facebook 5 Bloomberg 4 Amazon 2 Uber 2 Google 2 TikTok 3 Adobe 2 Apple 2 ByteDance 3 Microsoft 2 Grab 2
# https://leetcode.com/problems/remove-invalid-parentheses/

# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

# Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

# Example 1:
# Input: s = "()())()"
# Output: ["(())()","()()()"]
# Example 2:
# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]
# Example 3:
# Input: s = ")("
# Output: [""]
from ast import List
from collections import deque

# https://leetcode.com/problems/remove-invalid-parentheses/solutions/75032/share-my-java-bfs-solution/
# The idea is straightforward, with the input string s, we generate all possible states by removing one ( or ),
# check if they are valid, if found valid ones on the current level, put them to the final result list
# and we are done, otherwise, add them to a queue and carry on to the next level.

# The good thing of using BFS is that we can guarantee the number of parentheses that need to be removed is minimal,
# also no recursion call is needed in BFS.
# BFS time O(n * 2^(n-1)) where total 2^(n-1) substrings and each check cost n
class RemoveInvalidParentheses:
    OPEN = "("
    CLOSE = ")"

    def removeInvalidParentheses(self, s: str) -> List[str]:
        results = list()
        if not s:
            return results

        visited = set()
        visited.add(s)
        queue = deque()
        queue.append(s)

        found = False
        while queue:
            removed = queue.popleft()
            if self.is_valid(removed):
                # found an answer
                results.append(removed)
                found = True

            if found:
                continue

            for i, character in enumerate(removed):
                if character != self.OPEN and character != self.CLOSE:
                    continue

                next_removed = removed[:i] + removed[i + 1 :]
                if next_removed in visited:
                    continue

                queue.append(next_removed)
                visited.add(next_removed)

        return results

    def is_valid(self, s: str) -> bool:
        count = 0  # should never < 0 and should be 0 by the end

        for character in s:
            if character == self.OPEN:
                count += 1
            if character == self.CLOSE:
                count -= 1
                if count == -1:
                    return False

        return count == 0
