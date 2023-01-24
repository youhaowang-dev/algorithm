# Linked List, Recursion
# Apple 2 Google 4 Amazon 3 Adobe 3 Bloomberg 2 Facebook 12 Microsoft 5
# https://leetcode.com/problems/remove-linked-list-elements/
# Given the head of a linked list and an integer val, 
# remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
class RemoveLinkedListElements:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # TODO
